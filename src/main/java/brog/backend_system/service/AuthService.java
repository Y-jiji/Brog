package brog.backend_system.service;

import brog.backend_system.entity.request.GenCaptchaBody;
import brog.backend_system.entity.request.LoginBody;
import brog.backend_system.entity.request.RegisterBody;
import brog.backend_system.entity.response.StatusInfoMessage;
import org.springframework.http.ResponseEntity;

import javax.servlet.http.HttpServletResponse;

public interface AuthService {
    ResponseEntity<StatusInfoMessage> login(LoginBody body, HttpServletResponse response);

    ResponseEntity<StatusInfoMessage> register(RegisterBody body);

    ResponseEntity<StatusInfoMessage> genCaptcha(GenCaptchaBody body);
}
