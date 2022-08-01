package brog.backend_system.service.impl;

import brog.backend_system.entity.request.LoginBody;
import brog.backend_system.entity.request.RegisterBody;
import brog.backend_system.entity.response.StatusInfoMessage;
import brog.backend_system.mapper.AccountMapper;
import brog.backend_system.service.AuthService;
import lombok.AllArgsConstructor;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Service;

@Service
@AllArgsConstructor
public class AuthServiceImpl implements AuthService {
    AccountMapper accountMapper;

    @Override
    public ResponseEntity<StatusInfoMessage> login(LoginBody body) {
        String account = body.getAccount();
        String password = body.getPassword();

        return new ResponseEntity<>(
                new StatusInfoMessage(1, "ok"),
                HttpStatus.OK
        );
    }

    @Override
    public ResponseEntity<StatusInfoMessage> register(RegisterBody body) {
        String username = body.getUsername();
        String email = body.getEmail();
        String password = body.getPassword();

        return new ResponseEntity<>(
                new StatusInfoMessage(1, "ok"),
                HttpStatus.OK
        );
    }
}
