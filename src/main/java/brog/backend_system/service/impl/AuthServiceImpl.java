package brog.backend_system.service.impl;

import brog.backend_system.entity.Account;
import brog.backend_system.entity.Captcha;
import brog.backend_system.entity.request.GenCaptchaBody;
import brog.backend_system.entity.request.LoginBody;
import brog.backend_system.entity.request.RegisterBody;
import brog.backend_system.entity.response.StatusInfoMessage;
import brog.backend_system.mapper.AccountMapper;
import brog.backend_system.mapper.CaptchaMapper;
import brog.backend_system.service.AuthService;
import brog.backend_system.util.JWTUtils;
import com.baomidou.mybatisplus.core.conditions.query.LambdaQueryWrapper;
import lombok.AllArgsConstructor;
import org.springframework.http.HttpHeaders;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.mail.SimpleMailMessage;
import org.springframework.mail.javamail.JavaMailSender;
import org.springframework.stereotype.Service;

import java.util.Date;
import java.util.Random;

@Service
@AllArgsConstructor
public class AuthServiceImpl implements AuthService {
    AccountMapper accountMapper;
    CaptchaMapper captchaMapper;

    JavaMailSender mailSender;
    JWTUtils jwtUtils;

    @Override
    public ResponseEntity<StatusInfoMessage> login(LoginBody body) {
        String account = body.getAccount();
        String password = body.getPassword();
        Account accountInTable = accountMapper.selectOne(
                new LambdaQueryWrapper<Account>().eq(Account::getUsername, account).eq(Account::getPassword, password)
        );
        if(accountInTable == null){
            return new ResponseEntity<>(
                    new StatusInfoMessage(2, "Username doesn't exists or password incorrect"),
                    HttpStatus.NOT_ACCEPTABLE
            );
        }
        Long userId = accountInTable.getId();
        String token = jwtUtils.createToken(userId.toString(), 1800);
        accountInTable.setToken(token);
        accountMapper.updateById(accountInTable);
        HttpHeaders headers = new HttpHeaders();
        headers.add("token", token);
        return new ResponseEntity<>(
                new StatusInfoMessage(1, token),
                headers,
                HttpStatus.OK
        );
    }

    @Override
    public ResponseEntity<StatusInfoMessage> register(RegisterBody body) {
        String username = body.getUsername();
        String email = body.getEmail();
        String password = body.getPassword();
        String captcha = body.getCaptcha();

        Captcha captchaEntity = captchaMapper.selectById(email);
        if ((captchaEntity == null) || (!captcha.equals(captchaEntity.getCaptcha())) || (System.currentTimeMillis() > captchaEntity.getExpire().getTime())) {
            return new ResponseEntity<>(
                    new StatusInfoMessage(3, "Captcha doesn't match"),
                    HttpStatus.NOT_ACCEPTABLE
            );
        }

        Account accountInTable = accountMapper.selectOne(
                new LambdaQueryWrapper<Account>().eq(Account::getUsername, username)
        );
        if(accountInTable != null){
            return new ResponseEntity<>(
                    new StatusInfoMessage(2, "Username already exists"),
                    HttpStatus.NOT_ACCEPTABLE
            );
        }

        Account accountEntity = new Account();
        accountEntity.setUsername(username);
        accountEntity.setEmail(email);
        accountEntity.setPassword(password);
        accountMapper.insert(accountEntity);

        return new ResponseEntity<>(
                new StatusInfoMessage(1, "ok"),
                HttpStatus.OK
        );
    }

    @Override
    public ResponseEntity<StatusInfoMessage> genCaptcha(GenCaptchaBody body) {
        String email = body.getEmail();
        Random random = new Random();
        Integer captcha = 100000 + random.nextInt(900000);
        Date expireTime = new Date(System.currentTimeMillis() + 120000);
        Captcha captchaInTable = captchaMapper.selectById(email);
        if(captchaInTable == null) {
            Captcha captchaEntity = new Captcha(email, captcha.toString(), expireTime);
            captchaMapper.insert(captchaEntity);
        }
        else{
            captchaInTable.setCaptcha(captcha.toString());
            captchaInTable.setExpire(expireTime);
            captchaMapper.updateById(captchaInTable);
        }
        SimpleMailMessage mailMessage = new SimpleMailMessage();
        mailMessage.setText("[Brog] 您的邮箱验证码为：" + captcha);
        mailMessage.setSubject("[Brog]Brog注册邮箱验证");
        mailMessage.setTo(email);
        mailMessage.setFrom("gonggongjohn@163.com");
        mailSender.send(mailMessage);

        return new ResponseEntity<>(
                new StatusInfoMessage(1, "ok"),
                HttpStatus.OK
        );
    }
}
