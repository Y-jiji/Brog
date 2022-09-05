package brog.backend_system.service.impl;

import brog.backend_system.entity.Account;
import brog.backend_system.entity.Profile;
import brog.backend_system.entity.response.ProfileMessage;
import brog.backend_system.entity.response.StatusInfoMessage;
import brog.backend_system.mapper.AccountMapper;
import brog.backend_system.mapper.ProfileMapper;
import brog.backend_system.service.ProfileService;
import brog.backend_system.util.JWTUtils;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Service;
import org.springframework.web.multipart.MultipartFile;

import java.io.File;
import java.io.IOException;
import java.util.UUID;

@Service
public class ProfileServiceImpl implements ProfileService {
    @Value("${profile.avatar}")
    private String avatarRootPath;
    private AccountMapper accountMapper;
    private ProfileMapper profileMapper;
    private JWTUtils jwtUtils;

    public ProfileServiceImpl(AccountMapper accountMapper, ProfileMapper profileMapper, JWTUtils jwtUtils){
        this.accountMapper = accountMapper;
        this.profileMapper = profileMapper;
        this.jwtUtils = jwtUtils;
    }

    @Override
    public ResponseEntity<ProfileMessage> getProfile(String token) {
        Long userId = jwtUtils.parseAndGetId(token);
        Account userEntity = accountMapper.selectById(userId);
        if(userEntity == null){
            return new ResponseEntity<>(
                    new ProfileMessage(999, null),
                    HttpStatus.INTERNAL_SERVER_ERROR
            );
        }
        String username = userEntity.getUsername();
        Profile profileEntity = profileMapper.selectById(username);
        if(profileEntity == null){
            return new ResponseEntity<>(
                    new ProfileMessage(999, null),
                    HttpStatus.INTERNAL_SERVER_ERROR
            );
        }
        return new ResponseEntity<>(
                new ProfileMessage(1, profileEntity),
                HttpStatus.OK
        );
    }

    @Override
    public ResponseEntity<StatusInfoMessage> setAvatar(String token, MultipartFile avatar) {
        Long userId = jwtUtils.parseAndGetId(token);
        Account userEntity = accountMapper.selectById(userId);
        if(userEntity == null){
            return new ResponseEntity<>(
                    new StatusInfoMessage(999, "Error occurred when saving file to server"),
                    HttpStatus.INTERNAL_SERVER_ERROR
            );
        }
        String username = userEntity.getUsername();
        String originalFilename = avatar.getOriginalFilename();
        String suffix = originalFilename.substring(originalFilename.lastIndexOf("."));
        String saveFilename = UUID.randomUUID().toString() + suffix;
        File rootDir = new File(avatarRootPath);
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
            avatar.transferTo(new File(avatarRootPath + saveFilename));
        } catch (IOException e){
            e.printStackTrace();
            return new ResponseEntity<>(
                    new StatusInfoMessage(999, "Error occurred when saving file to server"),
                    HttpStatus.INTERNAL_SERVER_ERROR
            );
        }
        Profile profileEntity = profileMapper.selectById(username);
        if(profileEntity == null){
            return new ResponseEntity<>(
                    new StatusInfoMessage(999, "Error occurred when saving file to server"),
                    HttpStatus.INTERNAL_SERVER_ERROR
            );
        }
        profileEntity.setAvatar(saveFilename);
        profileMapper.updateById(profileEntity);
        return new ResponseEntity<>(
                new StatusInfoMessage(1, "ok"),
                HttpStatus.OK
        );
    }
}
