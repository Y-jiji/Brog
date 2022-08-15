package brog.backend_system.service;

import brog.backend_system.entity.response.MaterialListMessage;
import brog.backend_system.entity.response.StatusInfoMessage;
import org.springframework.http.ResponseEntity;
import org.springframework.web.multipart.MultipartFile;

public interface CommunityService {
    ResponseEntity<StatusInfoMessage> uploadMaterial(String token, Integer type, String title, MultipartFile file);

    ResponseEntity<MaterialListMessage> listMaterial();

    ResponseEntity<StatusInfoMessage> addProperty(String token, String mid);
}
