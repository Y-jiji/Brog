package brog.backend_system.controller;

import brog.backend_system.entity.request.GenCaptchaBody;
import brog.backend_system.entity.request.LoginBody;
import brog.backend_system.entity.request.RegisterBody;
import brog.backend_system.entity.response.StatusInfoMessage;
import brog.backend_system.service.AuthService;
import lombok.AllArgsConstructor;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

@CrossOrigin
@RestController
@RequestMapping("/auth")
@AllArgsConstructor
public class AuthController {
    AuthService authService;

    @PostMapping("/login")
    public ResponseEntity<StatusInfoMessage> login(@RequestBody LoginBody body){
        return authService.login(body);
    }

    @PostMapping("/register")
    public ResponseEntity<StatusInfoMessage> register(@RequestBody RegisterBody body){
        return authService.register(body);
    }

    @PostMapping("/gen_captcha")
    public ResponseEntity<StatusInfoMessage> genCaptcha(@RequestBody GenCaptchaBody body){
        return authService.genCaptcha(body);
    }
}
