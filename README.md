
# SAMPLE SCORE for check return type

#### requirement 
```
Docker
chrome browser
ICONex wallet
```

#### Step
##### 1. start T-Bears docker container
`$ docker run -it --name tbears -p 9000:9000 iconloop/tbears:mainnet`  
##### 2. pull this repo[in docker container]
`$ git clone https://github.com/nanaones/score-external-return-test`
##### 3. deploy with T-Bears
`$ cd ./score-external-return-test` . 

`$ tbears deploy -k ./keystore_test1 ./test` . 

`Input your keystore password: ` . 

Keystore password is `test1_Account`
then, you can see


``
Send deploy request successfully.
If you want to check SCORE deployed successfully, execute txresult command
transaction hash: 0xcd948ebdb5aa158b399f50963be87e921acdaabdd93a68481a535b038ac4b91e
``
  
  
**copy transaction hash**


##### 4. check SCORE address
   `$ tbears txresult [type txhash]` . 
   
   like this  
   
   `$ tbears txresult 0xcd948ebdb5aa158b399f50963be87e921acdaabdd93a68481a535b038ac4b91e`

##### 5. check it on ICONex(in chrome browser)
   [how to change network](https://www.icondev.io/docs/how-to-change-network-in-iconex)


---

 ### Set network
 ![img](/pic/icon.png)



 ### Then, you can see your contract method on ICONex

 #### move to contract tab & paste contract address.  
 
 ![img](/pic/contract.png)



 #### you can see return values.  
 
 ## Type bool
 ![img](/pic/bool.png) . 
 
 ## Type dict
 ![img](/pic/dict.png) . 
 
 ## Type int
 ![img](/pic/int.png) . 
 
 ## Type list
 ![img](/pic/list.png)

