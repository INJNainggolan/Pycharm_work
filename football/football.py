import random
import numpy as np

def match(score_x, score_y, int_w, int_z):
    if(score_x > score_y):
        int_w = int_w + 3
        int_z = int_z + 0
        Score_Integral = [score_x, score_y, int_w, int_z]
        return Score_Integral
    elif(score_x == score_y):
        int_w = int_w + 1
        int_z = int_z + 1
        Score_Integral = [score_x, score_y, int_w, int_z]
        return Score_Integral
    else:
        int_w = int_w + 0
        int_z = int_z + 3
        Score_Integral = [score_x, score_y, int_w, int_z]
        return Score_Integral

if __name__=="__main__":
    #**葡萄牙 德国 西班牙 阿根廷**

    Portugal_int = 0
    Germany_int = 0
    Spain_int = 0
    Argentina_int = 0

    #*********************************************************************#
    print("*****第一场比赛 葡萄牙vs德国")

    Integral_total = [Portugal_int, Germany_int, Spain_int, Argentina_int]
    print("           葡萄牙 德国 西班牙 阿根廷")
    print("第一场赛前积分表",Integral_total)

    Portugal_score = random.randrange(0, 10)
    Germany_score = random.randrange(0, 10)

    Score_Integral = match(Portugal_score, Germany_score, Portugal_int, Germany_int)
    Portugal_int = Score_Integral[2]
    Germany_int = Score_Integral[3]
    print("葡萄牙vs德国 ", Score_Integral[0],":",Score_Integral[1])
    print("Portugal的积分为：", Score_Integral[2])
    print("Germany的积分为：", Score_Integral[3])

    Integral_total = [Portugal_int, Germany_int, Spain_int, Argentina_int]
    print("           葡萄牙 德国 西班牙 阿根廷")
    print("第一场赛后积分表", Integral_total)



    # *********************************************************************#
    print("\n*****第二场比赛 西班牙vs阿根廷")

    Integral_total = [Portugal_int, Germany_int, Spain_int, Argentina_int]
    print("           葡萄牙 德国 西班牙 阿根廷")
    print("第二场赛前积分表", Integral_total)

    Spain_score = random.randrange(0, 10)
    Argentina_score = random.randrange(0, 10)

    Score_Integral = match(Spain_score, Argentina_score, Spain_int, Argentina_int)
    Spain_int = Score_Integral[2]
    Argentina_int = Score_Integral[3]
    print("西班牙vs阿根廷 ", Score_Integral[0], ":", Score_Integral[1])
    print("Spain的积分为：", Score_Integral[2])
    print("Argentina的积分为：", Score_Integral[3])
    Integral_total = [Portugal_int, Germany_int, Spain_int, Argentina_int]
    print("           葡萄牙 德国 西班牙 阿根廷")
    print("第二场赛后积分表", Integral_total)



    # *********************************************************************#
    print("\n*****第三场比赛 葡萄牙vs西班牙")

    Integral_total = [Portugal_int, Germany_int, Spain_int, Argentina_int]
    print("           葡萄牙 德国 西班牙 阿根廷")
    print("第三场赛前积分表", Integral_total)

    Portugal_score = random.randrange(0, 10)
    Spain_score = random.randrange(0, 10)

    Score_Integral = match(Portugal_score, Spain_score, Portugal_int, Spain_int)
    Portugal_int = Score_Integral[2]
    Spain_int = Score_Integral[3]
    print("葡萄牙vs西班牙 ", Score_Integral[0], ":", Score_Integral[1])
    print("Portugal的积分为：", Score_Integral[2])
    print("Spain的积分为：", Score_Integral[3])
    Integral_total = [Portugal_int, Germany_int, Spain_int, Argentina_int]
    print("           葡萄牙 德国 西班牙 阿根廷")
    print("第三场赛后积分表", Integral_total)



    # *********************************************************************#
    print("\n*****第四场比赛 德国vs阿根廷")

    Integral_total = [Portugal_int, Germany_int, Spain_int, Argentina_int]
    print("           葡萄牙 德国 西班牙 阿根廷")
    print("第四场赛前积分表", Integral_total)

    Germany_score = random.randrange(0, 10)
    Argentina_score = random.randrange(0, 10)

    Score_Integral = match(Germany_score, Argentina_score, Germany_int, Argentina_int)
    Germany_int = Score_Integral[2]
    Argentina_int = Score_Integral[3]
    print("德国vs阿根廷 ", Score_Integral[0], ":", Score_Integral[1])
    print("Germany的积分为：", Score_Integral[2])
    print("Argentina的积分为：", Score_Integral[3])
    Integral_total = [Portugal_int, Germany_int, Spain_int, Argentina_int]
    print("           葡萄牙 德国 西班牙 阿根廷")
    print("第四场赛后积分表", Integral_total)



    # *********************************************************************#
    print("\n*****第五场比赛 葡萄牙vs阿根廷")

    Integral_total = [Portugal_int, Germany_int, Spain_int, Argentina_int]
    print("           葡萄牙 德国 西班牙 阿根廷")
    print("第五场赛前积分表", Integral_total)

    Portugal_score = random.randrange(0, 10)
    Argentina_score = random.randrange(0, 10)

    Score_Integral = match(Portugal_score, Argentina_score, Portugal_int, Argentina_int)
    Portugal_int = Score_Integral[2]
    Argentina_int = Score_Integral[3]
    print("葡萄牙vs阿根廷 ", Score_Integral[0], ":", Score_Integral[1])
    print("Portugal的积分为：", Score_Integral[2])
    print("Argentina的积分为：", Score_Integral[3])
    Integral_total = [Portugal_int, Germany_int, Spain_int, Argentina_int]
    print("           葡萄牙 德国 西班牙 阿根廷")
    print("第五场赛后积分表", Integral_total)

    # *********************************************************************#
    print("\n*****第六场比赛 德国vs西班牙")

    Integral_total = [Portugal_int, Germany_int, Spain_int, Argentina_int]
    print("           葡萄牙 德国 西班牙 阿根廷")
    print("第六场赛前积分表", Integral_total)

    Germany_score = random.randrange(0, 10)
    Spain_score = random.randrange(0, 10)

    Score_Integral = match(Germany_score, Spain_score, Germany_int, Spain_int)
    Germany_int = Score_Integral[2]
    Spain_int = Score_Integral[3]
    print("德国vs西班牙 ", Score_Integral[0], ":", Score_Integral[1])
    print("Germany的积分为：", Score_Integral[2])
    print("Spain的积分为：", Score_Integral[3])
    Integral_total = [Portugal_int, Germany_int, Spain_int, Argentina_int]
    print("           葡萄牙 德国 西班牙 阿根廷")
    print("第六场赛后积分表", Integral_total)

    numpy.max(list)