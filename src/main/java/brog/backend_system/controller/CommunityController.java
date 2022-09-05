package brog.backend_system.controller;

import brog.backend_system.entity.request.MaterialIdBody;
import brog.backend_system.entity.response.MaterialListMessage;
import brog.backend_system.entity.response.StatusInfoMessage;
import brog.backend_system.service.CommunityService;
import lombok.AllArgsConstructor;
import org.springframework.http.ResponseEntity;
import org.springframework.transaction.annotation.Transactional;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.multipart.MultipartFile;

@CrossOrigin
@RestController
@RequestMapping("/community")
@AllArgsConstructor
@Transactional
public class CommunityController {
    CommunityService communityService;

    @PostMapping("/upload_material")
    public ResponseEntity<StatusInfoMessage> uploadMaterial(@RequestHeader String token, @RequestParam Integer type, @RequestParam String title, @RequestParam MultipartFile file){
        return communityService.uploadMaterial(token, type, title, file);
    }

    @GetMapping("/list_material")
    public ResponseEntity<MaterialListMessage> listMaterial(){
        return communityService.listMaterial();
    }

    @PostMapping("/add_property")
    public ResponseEntity<StatusInfoMessage> addProperty(@RequestHeader String token, @RequestBody MaterialIdBody body){
        return communityService.addProperty(token, body.getMid());
    }
}
