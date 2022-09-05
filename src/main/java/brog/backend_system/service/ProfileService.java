package brog.backend_system.service;

import brog.backend_system.entity.response.ProfileMessage;
import brog.backend_system.entity.response.StatusInfoMessage;
import org.springframework.http.ResponseEntity;
import org.springframework.web.multipart.MultipartFile;

public interface ProfileService {
    ResponseEntity<ProfileMessage> getProfile(String token);
    ResponseEntity<StatusInfoMessage> setAvatar(String token, MultipartFile avatar);
}
