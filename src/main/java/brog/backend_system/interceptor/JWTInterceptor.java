package brog.backend_system.interceptor;

import brog.backend_system.util.JWTUtils;
import io.jsonwebtoken.Claims;
import lombok.AllArgsConstructor;
import org.springframework.http.HttpStatus;
import org.springframework.web.servlet.HandlerInterceptor;

import javax.servlet.http.Cookie;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

@AllArgsConstructor
public class JWTInterceptor implements HandlerInterceptor {
    JWTUtils jwtUtils;

    @Override
    public boolean preHandle(HttpServletRequest request, HttpServletResponse response, Object handler) throws Exception {
        Cookie[] cookies = request.getCookies();
        for(Cookie cookie : cookies){
            if(cookie.getName().equals("token")){
                String token = cookie.getValue();
                if(token == null){
                    response.setStatus(HttpStatus.UNAUTHORIZED.value());
                    return false;
                }
                Claims parsedToken = jwtUtils.parseToken(token);
                if(parsedToken == null || jwtUtils.hasExpired(parsedToken)){
                    response.setStatus(HttpStatus.UNAUTHORIZED.value());
                    return false;
                }
                return true;
            }
        }
        //String token = request.getHeader("token");
        response.setStatus(HttpStatus.UNAUTHORIZED.value());
        return false;
    }
}
