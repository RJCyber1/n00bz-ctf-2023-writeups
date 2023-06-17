We can follow the following steps to get the flag:

1. copy and paste the given script into remix
![image](https://github.com/RJCyber1/n00bz-ctf-2023-writeups/assets/86359182/c213dca9-1270-4cf7-b693-f99173b14106)

2. compile and then deploy the script given in the description
![image](https://github.com/RJCyber1/n00bz-ctf-2023-writeups/assets/86359182/9b3860fe-65c9-43fc-bb7c-63792f57972c)

3. set value on remix to 110

![image](https://github.com/RJCyber1/n00bz-ctf-2023-writeups/assets/86359182/b5f3b245-7278-44a6-9a46-0f1e902f1185)

4. set buy amount to 1 and click all buttons (press buy, setprice and solve after each other on the remix ide)
![image](https://github.com/RJCyber1/n00bz-ctf-2023-writeups/assets/86359182/d7c0c5e5-f36f-479e-8702-ae57c15146e0)

5. copy the solve transaction hash into cyberchef (0x9a51d4efe2f23f207e48c5b0f7463d7349150059603809493ce1669e73cdbd94)
![image](https://github.com/RJCyber1/n00bz-ctf-2023-writeups/assets/86359182/ea5e7511-7ddc-45b4-bc9a-bf9cd3682640)

6. xor with given value (575105531e4f120e1c6d115d5d126d5d4e3a43590f59074439425a525616515f5b4e4c5b000057434d475b416f4e5b57473c0848694158095b56173b170a5d51) in description to get the flag
![image](https://github.com/RJCyber1/n00bz-ctf-2023-writeups/assets/86359182/a0de905b-54eb-4feb-a089-9e4d7825da3a)


