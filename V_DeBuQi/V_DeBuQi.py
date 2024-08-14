#!/usr/bin/env python3
# -*- coding:utf-8 -*-

G_propertySET = {"RESPECT", "FORCE", "PRICE"}
World_x = ""
World_y = ""
World_p = ""


class InputOBJ:
    def __init__(self, inputSTR):
        global World_x
        global World_y
        global World_p

        self.inputSTR = inputSTR
        self.obj = inputSTR.split("起")[-1]
        World_y = self.obj
        if "得" in self.inputSTR:
            self.subj = inputSTR.split("得")[0][:-1]
            self.v = inputSTR.split("得")[0][-1]
        elif "不" in self.inputSTR:
            self.subj = inputSTR.split("不")[0][:-1]
            self.v = inputSTR.split("不")[0][-1]
        World_x = self.subj
        self.has_ego = False
        self.w(self.obj)
        self.property = self.PROPERTY(World_p)
        World_p = self.property
        return None

    def PROPERTY(self, p):
        if self.v in "看瞧":
            if self.has_ego == True:
                p = "RESPECT"
            elif self.has_ego == False:
                p = "PRICE"
            else:
                p = "???"
        else:
            if self.v in "抬舉揚抱扛擔掀提":
                p = "FORCE"
            else:
                p = "PRICE"
        return p

    def w(self, obj):
        if self.obj[-1] in "你我他她妳":
            self.has_ego = True
        elif self.obj[-1] in "者人":
            if any(x in set(self.inputSTR.split("起")[-1]) for x in ("的這那你我他她妳")):
                self.has_ego = True
            else:
                self.has_ego = None
        else:
            self.has_ego = False

    def anthropomorphize(self, obj):
        self.has_ego = True

def EVAL(inputObj):
    if inputObj.property in G_propertySET:
        if inputObj.has_ego in {True, False}:
            if V(inputObj.subj, GIVE(inputObj.property, inputObj.obj)):
                return True
            else:
                return False
        else:
            return None
    else:
        return True

def V(subj, GIVE):
    if subj == World_x:
        if World_y == inputObj.obj:
            return True
        else:
            return False
    else:
        return True

def GIVE(p, y):
    if p == World_p and y == World_y:
        return True
    else:
        return False




#def V_DeBu_Qi(subj, obj, p):
    #EVAL(subj, obj, p)

if __name__ == "__main__":
    print("\n")
    inputObj = InputOBJ("我看不起這種人")
    V_DeQi = EVAL(inputObj)
    print(f"[[{inputObj.inputSTR}]] => V-得/不起 Meaning:{inputObj.property}\n")

    inputObj = InputOBJ("他瞧不起我")
    V_DeQi = EVAL(inputObj)
    print(f"[[{inputObj.inputSTR}]]     => V-得/不起 Meaning:{inputObj.property}\n")

    inputObj = InputOBJ("我最看得起人")
    V_DeQi = EVAL(inputObj)
    print(f"[[{inputObj.inputSTR}]]   => V-得/不起 Meaning:{inputObj.property}\n")

    inputObj = InputOBJ("我抬得起電冰箱")
    V_DeQi = EVAL(inputObj)
    print(f"[[{inputObj.inputSTR}]] => V-得/不起 Meaning:{inputObj.property}\n")

    inputObj = InputOBJ("我舉不起洗衣機")
    V_DeQi = EVAL(inputObj)
    print(f"[[{inputObj.inputSTR}]] => V-得/不起 Meaning:{inputObj.property}\n")

    inputObj = InputOBJ("我買不起蘋果電腦")
    V_DeQi = EVAL(inputObj)
    print(f"[[{inputObj.inputSTR}]] => V-得/不起 Meaning:{inputObj.property}\n")

    inputObj = InputOBJ("我買得起蘋果電腦")
    V_DeQi = EVAL(inputObj)
    print(f"[[{inputObj.inputSTR}]] => V-得/不起 Meaning:{inputObj.property}\n")
