package brog.backend_system.controller;

import brog.backend_system.entity.response.ProfileMessage;
import brog.backend_system.entity.response.StatusInfoMessage;
import brog.backend_system.service.ProfileService;
import lombok.AllArgsConstructor;
import org.springframework.http.ResponseEntity;
import org.springframework.transaction.annotation.Transactional;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.multipart.MultipartFile;

@CrossOrigin
@RestController
@RequestMapping("/profile")
@AllArgsConstructor
@Transactional
public class ProfileController {
    ProfileService profileService;

    @GetMapping("/get_profile")
    public ResponseEntity<ProfileMessage> getProfile(@RequestHeader String token){
        return profileService.getProfile(token);
    }

    @PostMapping("/set_avatar")
    public ResponseEntity<StatusInfoMessage> setAvatar(@RequestHeader String token, @RequestParam MultipartFile avatar){
        return profileService.setAvatar(token, avatar);
    }
}
