package brog.backend_system.service.impl;

import brog.backend_system.entity.Account;
import brog.backend_system.entity.Material;
import brog.backend_system.entity.Shelf;
import brog.backend_system.entity.response.MaterialListMessage;
import brog.backend_system.entity.response.StatusInfoMessage;
import brog.backend_system.mapper.AccountMapper;
import brog.backend_system.mapper.MaterialMapper;
import brog.backend_system.mapper.ShelfMapper;
import brog.backend_system.service.CommunityService;
import brog.backend_system.util.JWTUtils;
import com.baomidou.mybatisplus.extension.plugins.pagination.Page;
import io.jsonwebtoken.Claims;
import lombok.AllArgsConstructor;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Service;
import org.springframework.web.multipart.MultipartFile;

import java.io.File;
import java.io.IOException;
import java.util.List;
import java.util.UUID;

@Service
public class CommunityServiceImpl implements CommunityService {
    @Value("${material.rootpath}")
    private String materialRootPath;
    private AccountMapper accountMapper;
    private MaterialMapper materialMapper;
    private ShelfMapper shelfMapper;
    private JWTUtils jwtUtils;

    /** This class cannot @AllArgsConstructor since it has a @Value var */
    public CommunityServiceImpl(AccountMapper accountMapper, MaterialMapper materialMapper, ShelfMapper shelfMapper, JWTUtils jwtUtils){
        this.accountMapper = accountMapper;
        this.materialMapper = materialMapper;
        this.shelfMapper = shelfMapper;
        this.jwtUtils = jwtUtils;
    }

    @Override
    public ResponseEntity<StatusInfoMessage> uploadMaterial(String token, Integer type, String title, MultipartFile file) {
        Long userId = jwtUtils.parseAndGetId(token);
        Account userEntity = accountMapper.selectById(userId);
        if(userEntity == null){
            return new ResponseEntity<>(
                    new StatusInfoMessage(999, "Error occurred when saving file to server"),
                    HttpStatus.INTERNAL_SERVER_ERROR
            );
        }
        String username = userEntity.getUsername();
        String originalFilename = file.getOriginalFilename();
        String suffix = originalFilename.substring(originalFilename.lastIndexOf("."));
        String saveFilename = UUID.randomUUID().toString() + suffix;
        File rootDir = new File(materialRootPath);
        if(!rootDir.exists()){
            boolean isCreated = rootDir.mkdirs();
            if(!isCreated){
                return new ResponseEntity<>(
                        new StatusInfoMessage(999, "Error occurred when saving file to server"),
                        HttpStatus.INTERNAL_SERVER_ERROR
                );
            }
        }
        
        try {
            file.transferTo(new File(materialRootPath + saveFilename));
        } catch (IOException e){
            e.printStackTrace();
            return new ResponseEntity<>(
                    new StatusInfoMessage(999, "Error occurred when saving file to server"),
                    HttpStatus.INTERNAL_SERVER_ERROR
            );
        }
        Material materialEntity = new Material();
        materialEntity.setType(type);
        materialEntity.setQuality(1);
        materialEntity.setVisibility(1);
        materialEntity.setOwner(username);
        materialEntity.setTitle(title);
        materialEntity.setFilepath(saveFilename);
        materialMapper.insert(materialEntity);
        return new ResponseEntity<>(
                new StatusInfoMessage(1, "ok"),
                HttpStatus.OK
        );
    }

    @Override
    public ResponseEntity<MaterialListMessage> listMaterial() {
        List<Material> materialEntities = materialMapper.selectList(null);
        return new ResponseEntity<>(
                new MaterialListMessage(1, materialEntities),
                HttpStatus.OK
        );
    }

    @Override
    public ResponseEntity<StatusInfoMessage> addProperty(String token, String mid) {
        Long userId = jwtUtils.parseAndGetId(token);
        Account userEntity = accountMapper.selectById(userId);
        if(userEntity == null){
            return new ResponseEntity<>(
                    new StatusInfoMessage(999, "Error occurred when saving adding property"),
                    HttpStatus.INTERNAL_SERVER_ERROR
            );
        }
        String username = userEntity.getUsername();
        Material materialEntity = materialMapper.selectById(mid);
        if(materialEntity == null){
            return new ResponseEntity<>(
                    new StatusInfoMessage(999, "Error occurred when adding property"),
                    HttpStatus.INTERNAL_SERVER_ERROR
            );
        }
        Shelf shelfEntity = new Shelf();
        shelfEntity.setUser(username);
        shelfEntity.setMid(mid);
        shelfMapper.insert(shelfEntity);
        return new ResponseEntity<>(
                new StatusInfoMessage(1, "ok"),
                HttpStatus.OK
        );
    }
}
