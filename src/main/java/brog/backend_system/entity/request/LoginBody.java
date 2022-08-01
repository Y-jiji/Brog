package brog.backend_system.entity.request;

import lombok.Data;

@Data
public class LoginBody {
    private String account; /** Username or email address */
    private String password;
}
