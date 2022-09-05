package brog.backend_system.controller;

import brog.backend_system.entity.request.GenCaptchaBody;
import brog.backend_system.entity.request.LoginBody;
import brog.backend_system.entity.request.RegisterBody;
import brog.backend_system.entity.response.StatusInfoMessage;
import brog.backend_system.service.AuthService;
import lombok.AllArgsConstructor;
import org.springframework.http.ResponseEntity;
import org.springframework.transaction.annotation.Transactional;
import org.springframework.web.bind.annotation.*;

import javax.servlet.http.HttpServletResponse;

@CrossOrigin
@RestController
@RequestMapping("/auth")
@AllArgsConstructor
@Transactional
public class AuthController {
    AuthService authService;

    @PostMapping("/login")
    public ResponseEntity<StatusInfoMessage> login(@RequestBody LoginBody body, HttpServletResponse response){
        return authService.login(body, response);
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
