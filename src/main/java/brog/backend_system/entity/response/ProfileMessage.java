package brog.backend_system.entity.response;

import brog.backend_system.entity.Profile;
import lombok.AllArgsConstructor;
import lombok.Data;

@Data
@AllArgsConstructor
public class ProfileMessage {
    private int status;
    private Profile profile;
}
