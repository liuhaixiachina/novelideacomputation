__author__ = 'ocean'
# def toDiscardPhrase(phrase):
#     if phrase == '':
#         return True
#     uselesswordslist = ["prior","practical", "basic", "different", "simple", "successful", "current", "possible", "previous", "existing", "well-stablished", "independent", "particular", "usual", "new", "powerful", "main", "common", "detailed", "efficient", "good", "acceptable", "effective", "novel", "state-of-the-art", "useful", "modern", "unreliable", "additional", "methodological", "available", "recent", "general", "specific", "creative", "brief", "critical", "major", "second", "reasonable", "various", "personal", "latest" ,"interesting"]
#
#     solutioncuewords = [
#                 "simulation",
#                 "simulations",
#                 "way",
#                 "policy",
#                 "technique",
#                 "technology",
#                 "algorithm",
#                 "method",
#                 "methods",
#                 "approach",
#                 "model",
#                 "modeling",
#                 "theory",
#                 "theories",
#                 "solution",
#                 "analysis",
#                 "analyze",
#                 "analyzing",
#                 "learn",
#                 "study",
#                 "studies",
#                 "studied",
#                 "learn",
#                 "learning"]
#     strSplit = str(phrase).split()
#     l = len(strSplit)
#     if l == 2:
#         if strSplit[0] in uselesswordslist and strSplit[1] in solutioncuewords:
#             return True
#     return False
#
# print toDiscardPhrase("prior  technique")


import os
import codecs
from da import *
#folderpath = '/home/ocean/Downloads/lhx/PhDProject/IdeaComputPython/dataset/fake'
#folderpath = '/home/ocean/Downloads/lhx/PhDProject/IdeaComputPython/dataset/webofknowledge/agrometeorologyEcophysiology'
#folderpath = '/home/ocean/Downloads/lhx/PhDProject/IdeaComputPython/dataset/webofknowledge/BiotechnologyCropGenetics'
#folderpath = '/home/ocean/Downloads/lhx/PhDProject/IdeaComputPython/dataset/webofknowledge/BreedingAgronomy'
#folderpath = '/home/ocean/Downloads/lhx/PhDProject/IdeaComputPython/dataset/webofknowledge/NutritionBioproducts'
#folderpath = '/home/ocean/Downloads/lhx/PhDProject/IdeaComputPython/dataset/webofknowledge/socialeconomicpolicy'
#folderpath = '/home/ocean/Downloads/lhx/PhDProject/IdeaComputPython/dataset/Science'

folderpath = '/home/ocean/Downloads/lhx/PhDProject/IdeaComputPython/outputs/forTTest'


removednpFile = ''
problemnpFile = ''
solutionnpFile = ''
def SiftOutputs():
    for file in os.listdir(folderpath):
        if file.endswith(".txt"):
            with open(folderpath + '/'+file,'r') as doc:
                body = doc.read()
                newFile = parseAbstracts(body.lower())
                saveToCSV(newFile)

def parseAbstracts(abstracts):
    newFile = ''
    absList = abstracts.split(os.linesep)
    absDict = {}
    userid=''
    precision=''
    recall=''
    connectlines=''
    for a in absList:
        absDict[a.strip()] = m = {}
        if "Recommender IR Evaluator:".lower() in a.lower():
            connectlines=a.lower().split('[')[1]
            precision = connectlines.split(',')[0].lower().split(':')[1]
            recall = connectlines.split(',')[1].lower().split(':')[1].replace(']','')
            newFile += precision + ',' + recall + '\n'
    return newFile

def saveToCSV(myData):
    with codecs.open(folderpath + '/CON-20.csv', 'a', encoding='utf-8') as fr:
        fr.write(myData)

SiftOutputs()