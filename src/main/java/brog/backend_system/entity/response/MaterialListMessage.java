package brog.backend_system.entity.response;

import brog.backend_system.entity.Material;
import lombok.AllArgsConstructor;
import lombok.Data;

import java.util.List;

@Data
@AllArgsConstructor
public class MaterialListMessage {
    private int status;
    private List<Material> materials;
}
