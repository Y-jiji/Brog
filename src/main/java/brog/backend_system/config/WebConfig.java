package brog.backend_system.config;

import brog.backend_system.interceptor.JWTInterceptor;
import brog.backend_system.util.JWTUtils;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.context.annotation.Configuration;
import org.springframework.web.servlet.config.annotation.InterceptorRegistry;
import org.springframework.web.servlet.config.annotation.ResourceHandlerRegistry;
import org.springframework.web.servlet.config.annotation.WebMvcConfigurer;

@Configuration
public class WebConfig implements WebMvcConfigurer {
    @Value("${profile.avatar}")
    public String avatarRootPath;
    @Value("${material.rootpath}")
    public String materialRootPath;

    @Override
    public void addInterceptors(InterceptorRegistry registry) {
        registry.addInterceptor(new JWTInterceptor(new JWTUtils()))
                .addPathPatterns("/**")
                .excludePathPatterns(
                        "/auth/register",
                        "/auth/login",
                        "/auth/gen_captcha"
                );
    }

    @Override
    public void addResourceHandlers(ResourceHandlerRegistry registry) {
        registry.addResourceHandler("/file/avatar/**")
                .addResourceLocations("file:" + avatarRootPath);
        registry.addResourceHandler("/file/material/**")
                .addResourceLocations("file:" + materialRootPath);
    }
}
