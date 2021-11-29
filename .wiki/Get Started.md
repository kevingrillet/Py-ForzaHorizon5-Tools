* [Basic](#basic)
    1. [AutoWheelSpins](#autowheelspins)
    2. [AutoGPSDestination](#autogpsdestination)
    3. [AutoLabReplay](#autolabreplay)
    4. [AutoCarBuy](#autocarbuy)
    5. [AutoCarMastery](#autocarmastery)
        - [`2014 Ford Fiesta ST`](#2014-ford-fiesta-st)
        - [`1987 Pontiac Firebird Trans Am GTA`](#1987-pontiac-firebird-trans-am-gta)
        - [`2014 Porsche 911 Turbo S`](#2014-porsche-911-turbo-s)
    6. [AutoCarBuyLeastExpensive](#autocarbuyleastexpensive)
    7. [AutoRaceRestart](#autoracerestart)
    8. [AutoPhotoAllMyCars](#autoracerestart)
* [Advance](#advance)
    - [Just press z](#just-press-z)
    - [AutoCarBuy + AutoCarMastery + AutoLabReplay](#autocarbuy--autocarmastery--autolabreplay)
    - [AutoCarBuy + AutoCarMastery + AutoRaceRestart](#autocarbuy--autocarmastery--autoracerestart)
* [Dev](#dev)
    - [Dev tools](#dev-tools)
    - [Image debug](#image-debug)

## Basic

### AutoWheelSpins

Works fot WheelSpins and SuperWheelSpins!

Will spin until no more remain.

Will sell duplicates cars.

- Launch a first spin

  ![](https://user-images.githubusercontent.com/7203617/143293552-aab176f5-2a37-46ff-b417-a757b2ba81a9.jpg)

- Launch the script
- Set focus on Forza

### AutoGPSDestination

Will go to destination then press `esc`.

- SetUp full assist

  ![](https://user-images.githubusercontent.com/7203617/143285703-30f8c0ee-c8d8-42b8-aaa9-06734fde6ffc.jpg)

- Set your destination
- Launch the script
- Set focus on Forza

### AutoLabReplay

Can be used with `30` to quit game after max mastery points.

Will redo the last lab race done.

![](https://user-images.githubusercontent.com/7203617/143293466-835bca70-004b-498b-853d-511cf2d6b6b7.jpg)

Can be started from esc menu, esc menu in race or race preparation.

- SetUp full assist
- Launch the script
- Set focus on Forza

Example of codes from <https://www.youtube.com/watch?v=HPS8Ubziu7U>:

- 1 Lap | 206 340 638
- 15 Laps | 127 405 648
- 50 Laps | 430 730 853
- 50 Laps WITH MAX AI FOR CREDITS! | 473 350 397 

### AutoCarBuy

Buys car from collection.

- Place on the car you want to buy in car collection

  ![](https://user-images.githubusercontent.com/7203617/143294156-0c9c793d-3cbb-4f04-8396-8de6423ba5d0.jpg)

- Launch the script
- Set focus on Forza

### AutoCarMastery

Delete car after mastery, so it's **RISKY**!

#### `2014 Ford Fiesta ST`

Will get 10 Forzathon Points for 5 points: <https://youtu.be/zI3Sm7q34bs?t=13>

![](https://user-images.githubusercontent.com/7203617/143456768-e4c6a39d-ba7a-4391-85a6-c9f86ab28713.png)

The `2014 Ford Fiesta ST` needs to be the only car of the `Ford` constructor with filter `B` and `Hot Hatch`.

![](https://user-images.githubusercontent.com/7203617/143456955-41545796-77b0-4227-b962-1b2350aeae4c.png)

- At the home page of the house
- Launch the script
- Set focus on Forza

#### `1987 Pontiac Firebird Trans Am GTA`

Will get super wheelspins for 14 points: <https://youtu.be/HPS8Ubziu7U?t=140>

![](https://user-images.githubusercontent.com/7203617/143293559-7a901f3e-0450-44e4-a45e-4924d5381356.jpg)

The `1987 Pontiac Firebird Trans Am GTA` needs to be the 3rd car of the `Pontiac` constructor.

![](https://user-images.githubusercontent.com/7203617/143285495-8d88e725-64ee-4261-95fb-240b96b28ebe.jpg)

- At the home page of the house
- Launch the script
- Set focus on Forza

#### `2014 Porsche 911 Turbo S`

Will get super wheelspins for 11 points: <https://youtu.be/s6z0FyguhrI?t=30>

![](https://user-images.githubusercontent.com/7203617/143869702-1dfd2708-8b98-4fa1-adbe-72cdb09b0181.jpg)

The `2014 Porsche 911 Turbo S` needs to be the only car of the `Porsche` constructor with filter `A` and `Modern Sport Car`.

![](https://user-images.githubusercontent.com/7203617/143869701-09accdd1-e904-4375-9551-de9c6ce643d1.jpg)

- At the home page of the house
- Launch the script
- Set focus on Forza

### AutoCarBuyLeastExpensive

- At the home page of the house
- Launch the script
- Set focus on Forza

### AutoRaceRestart

Can be used with `70` to quit game after 100 restart.

Will restart the current race at the end.

Can be started from esc menu in race or race preparation.

![](https://user-images.githubusercontent.com/7203617/143869700-f018b844-598c-440f-9b48-56881decbe51.jpg)

- SetUp full assist
- Launch the script
- Set focus on Forza

Example of codes:

- 10sp in 30 secs | 743 324 179 | < <https://youtu.be/oBFlEdrj8Ec?t=16>>
- 10 sp in 30 sec straight road | 497 519 560 

### AutoPhotoAllMyCars

Can be used with `80` to quit game after done.

Need to be started from esc menu outside the house.

- Launch the script
- Set focus on Forza

## Advance

### Just press z

Choice `99`.

Will alt tab, press `esc`, then hold `z`

### AutoCarBuy + AutoCarMastery + AutoLabReplay

Choice `453`.

**Require to have a Lamborghini as favorite car, and be in it at the start.**

Need to be started from game default esc menu.

Will alt tab, check if max mastery, if `true` then AutoCarBuy + AutoCarMastery

Then loop
- AutoLabReplay
- Check mastery
- AutoCarBuy + AutoCarMastery

### AutoCarBuy + AutoCarMastery + AutoRaceRestart

Choice `457`.

**Require to have a Lamborghini as favorite car, and be in it at the start.**

Need to be started from game default esc menu.

Will alt tab, check if max mastery, if `true` then AutoCarBuy + AutoCarMastery

Then loop
- AutoRaceRestart (will run the last lab race)
- Check mastery
- AutoCarBuy + AutoCarMastery

## Dev

### Dev tools

Choice `0`.

### Image debug

Choice `98`.

Then choose your image to find.

```
Your choice:
98

List of images:
0_spins_remaining                        999_mastery                              999_super_wheelspins                     accolades                               
already_done                             autoshow                                 buy_car                                  cannot_afford_perk                      
car_already_owned                        collect_prize_and_spin_again             colors                                   ford                                    
ford_name                                ford_name_selected                       home                                     insufficient_cr                         
lamborghini_name                         lamborghini_name_selected                last_car_manufacturer_selected           loading_please_wait                     
my_cars                                  not_owned                                pontiac                                  pontiac_name                            
pontiac_name_selected                    porsche                                  porsche_name                             porsche_name_selected                   
processing_photo                         race_continue                            race_quit                                race_reward                             
race_skip                                race_start                               race_type                                skip                                    
value                                    value_menu                               value_selected

Choose image to search:
car_already_owned

find:                True
find_max_val:        0.9993559122085571
find_start:          (1072, 248)
find_end:            (1488, 301)
```

<hr>

<div align="center">
<a href="https://github.com/kevingrillet/Py-ForzaHorizon5-Tools/wiki/Requirements">Previous page</a>
|
<a href="https://github.com/kevingrillet/Py-ForzaHorizon5-Tools/wiki/Sources">Next page</a>
</div>
