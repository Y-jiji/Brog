package brog.backend_system.util;

import io.jsonwebtoken.Claims;
import io.jsonwebtoken.JwtException;
import io.jsonwebtoken.Jwts;
import io.jsonwebtoken.SignatureAlgorithm;
import io.jsonwebtoken.security.Keys;
import org.springframework.stereotype.Component;

import javax.crypto.SecretKey;
import java.nio.charset.StandardCharsets;
import java.util.Date;

@Component
public class JWTUtils {
    public String secret = "UCo2YzpiR3b3h7X1OjEbxc90aZyNBgTQcPqlJmIArw5ER1VkANTp74BWZjmDucf";

    public String createToken(String subject, int expire){
        Date issueTime = new Date();
        Date expireTime = new Date(issueTime.getTime() + expire * 1000L);
        SecretKey secretKey = Keys.hmacShaKeyFor(secret.getBytes(StandardCharsets.UTF_8));
        return Jwts
                .builder()
                .setIssuedAt(issueTime)
                .setSubject(subject)
                .setExpiration(expireTime)
                .signWith(secretKey)
                .compact();
    }

    public Claims parseToken(String token){
        Claims claims = null;
        SecretKey secretKey = Keys.hmacShaKeyFor(secret.getBytes(StandardCharsets.UTF_8));
        try {
            claims = Jwts
                    .parserBuilder()
                    .setSigningKey(secretKey)
                    .build()
                    .parseClaimsJwt(token)
                    .getBody();
        } catch (JwtException e){
            e.printStackTrace();
        }
        return claims;
    }

    public boolean hasExpired(Claims authorizer){
        Date expireTime = authorizer.getExpiration();
        return expireTime.before(new Date());
    }
}
