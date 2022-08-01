package brog.backend_system.util;

import io.jsonwebtoken.Jwts;
import io.jsonwebtoken.SignatureAlgorithm;
import io.jsonwebtoken.security.Keys;
import org.springframework.stereotype.Component;

import javax.crypto.SecretKey;
import java.nio.charset.StandardCharsets;
import java.util.Date;

@Component
public class JWTUtils {
    public String secret;

    public String createToken(int expire){
        Date issueTime = new Date();
        Date expireTime = new Date(issueTime.getTime() + expire * 1000L);
        SecretKey secretKey = Keys.hmacShaKeyFor(secret.getBytes(StandardCharsets.UTF_8));
        return Jwts
                .builder()
                .setIssuedAt(issueTime)
                .setExpiration(expireTime)
                .signWith(secretKey)
                .compact();
    }
}
