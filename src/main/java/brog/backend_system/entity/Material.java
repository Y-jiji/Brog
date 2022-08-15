package brog.backend_system.entity;

import com.baomidou.mybatisplus.annotation.IdType;
import com.baomidou.mybatisplus.annotation.TableId;
import com.baomidou.mybatisplus.annotation.TableName;
import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

@Data
@AllArgsConstructor
@NoArgsConstructor
@TableName("material")
public class Material {
    @TableId(type = IdType.ASSIGN_ID)
    private String id;
    private int type; /** Material type; 1 - Book, 2 - Paper, 3 - Note, 4 - Other document */
    private String owner;
    private int visibility; /** Material visibility; 1 - Private (Only owner can see), 2 - Public */
    private int quality; /** Quality of the material; 1 - Unlabeled, 2 - Community tagged, 3 - Expert reviewed */
    private String title;
    private String filepath;
}
