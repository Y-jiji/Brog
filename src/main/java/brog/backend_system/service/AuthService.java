package brog.backend_system.service;

import brog.backend_system.entity.request.LoginBody;
import brog.backend_system.entity.request.RegisterBody;
import brog.backend_system.entity.response.StatusInfoMessage;
import org.springframework.http.ResponseEntity;

public interface AuthService {
    ResponseEntity<StatusInfoMessage> login(LoginBody body);

    ResponseEntity<StatusInfoMessage> register(RegisterBody body);
}
