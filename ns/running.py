filename = ""
nowLine = 1


def Print(string):
    print(string)


class Pool(object):
    def __init__(self, name, type, value):
        self.name = name
        self.type = type
        self.value = value

class Stack(object):
    def __init__(self):
        self.stack = []
    def push(self, item):
        self.stack.append(item)
    def pop(self):
        if self.isEmpty():
            error(
                classes["error.UnknownError"],
                "There is a unknown error in the variable stack.",
                classes["error.fatal"]
            )
            return
        return self.stack.pop()
    def isEmpty(self):
        return len(self.stack) == 0


classes = {}
globalVars = {}
varStack = Stack()


def addVars(added): ...


def error(errorType, information, raiseType):
    RType = raiseType.value["vars"]["raiseType"]
    Print(
        "%s in line %d in %s:\n    %s: %s"
        % (
            raiseType.value["vars"]["raiseType"],
            nowLine,
            filename,
            errorType,
            information,
        )
    )
    if RType == "Fatal":
        stopProgram()
    elif RType == "Error":
        stopThreat()


def newVar(name, classType, value=None):
    if not classType in classes:
        error(
            classes["error.NameError"],
            'Cannot find the class "%s".' % classType,
            classes["error.fatal"]
        )
        return
    if name in globalVars:
        error(
            classes["error.RepeatedDefinitionError"],
            'Name "%s" was already defined.' % name,
            classes["error.error"]
        )
    varStack.push(name)
    if classType == "class" or classType == "function" or classType == "namespace":
        globalVars[name] = {
            "variable": Pool(name, "variable", (classes[classType], value["variable"])),
            "call": Pool(name, "code", (classes[classType], value["call"])),
        }
    else:
        globalVars[name] = Pool(name, "variable", (classes[classType], value))


def call(name, varList):
    for i in varList:
        globalVars[i] = varList[i]
    addVars()
    run(globalVars[name]["call"])


def splitKey(line): ...


def runLine(line):
    splitKey()


def run(): ...


def stopProgram(): ...


def stopThreat(): ...
