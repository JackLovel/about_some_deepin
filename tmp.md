### idea maven 配置国内源  
搜索 idea 文件夹下的所有`settings.xml` ， 并把下面的放到  `mirrors` 标签对内
```
      <mirror>  
            <id>alimaven</id>  
            <name>aliyun maven</name>  
            <url>http://maven.aliyun.com/nexus/content/groups/public/</url>  
            <mirrorOf>central</mirrorOf>          
       </mirror>
```
