package brog.backend_system.entity.request;

import lombok.Data;

@Data
public class RegisterBody {
    private String username;
    private String email;
    private String password;
}
