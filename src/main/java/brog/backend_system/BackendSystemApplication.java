package brog.backend_system;

import org.mybatis.spring.annotation.MapperScan;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
@MapperScan("brog.backend_system.mapper")
public class BackendSystemApplication {

    public static void main(String[] args) {
        SpringApplication.run(BackendSystemApplication.class, args);
    }

}
