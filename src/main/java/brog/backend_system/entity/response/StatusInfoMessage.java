package brog.backend_system.entity.response;

import lombok.AllArgsConstructor;
import lombok.Data;

@Data
@AllArgsConstructor
public class StatusInfoMessage {
    private int status;
    private String message;
}
