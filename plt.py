import matplotlib
import matplotlib.pyplot as plt
import numpy as np

def single(dfAcc, img='img.png', color1='blue', color2='orange'):
    labels = ['Normalizada', 'Inversa', 'Proporcional', 'PCA 70%', 'PCA 50%']
    acc = dfAcc['mean']
    dv = dfAcc['std']

    x = np.arange(len(labels))  # the label locations
    width = 0.35  # the width of the bars

    fig, ax = plt.subplots()
    rects1 = ax.bar(x - width/2, acc, width, color=color1)
    rects2 = ax.bar(x + width/2, dv, width, color=color2)

    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_ylabel('%')
    ax.set_ylim(0,100)
    #ax.set_title('Scores simples de cada base')
    ax.set_xticks(x)
    ax.set_xticklabels(labels)

    def autolabel(rects):
        """Attach a text label above each bar in *rects*, displaying its height."""
        for rect in rects:
            height = rect.get_height()
            ax.annotate('{}'.format(height),
                        xy=(rect.get_x() + rect.get_width() / 2, height),
                        xytext=(0, 3),  # 3 points vertical offset
                        textcoords="offset points",
                        ha='center', va='bottom')


    autolabel(rects1)
    autolabel(rects2)

    fig.tight_layout()

    plt.savefig(img)

def bagging(dfAcc, img='img.png', color1='#00FFFF', color2='#FF7F50'):
    labels = ['5', '10', '20', '30']
    acc = dfAcc['mean']
    dv = dfAcc['std']

    x = np.arange(len(labels))  # the label locations
    width = 0.35  # the width of the bars

    fig, ax = plt.subplots()
    rects1 = ax.bar(x - width/2, acc, width, color=color1)
    rects2 = ax.bar(x + width/2, dv, width, color=color2)

    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_ylabel('%')
    ax.set_ylim(0,100)
    #ax.set_title('Scores simples de cada base')
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.set_xlabel('Estimadores')

    def autolabel(rects):
        """Attach a text label above each bar in *rects*, displaying its height."""
        for rect in rects:
            height = rect.get_height()
            ax.annotate('{}'.format(height),
                        xy=(rect.get_x() + rect.get_width() / 2, height),
                        xytext=(0, 3),  # 3 points vertical offset
                        textcoords="offset points",
                        ha='center', va='bottom')


    autolabel(rects1)
    autolabel(rects2)

    fig.tight_layout()

    plt.savefig(img)
    
def voting(dfAcc, img='img.png', color1='blue', color2='orange'):
    labels = ['Normalizada', 'PCA 70%']
    acc = dfAcc['mean']
    dv = dfAcc['std']

    x = np.arange(len(labels))  # the label locations
    width = 0.35  # the width of the bars

    fig, ax = plt.subplots()
    rects1 = ax.bar(x - width/2, acc, width, color=color1)
    rects2 = ax.bar(x + width/2, dv, width, color=color2)

    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_ylabel('%')
    ax.set_ylim(0,100)
    #ax.set_title('Scores simples de cada base')
    ax.set_xticks(x)
    ax.set_xticklabels(labels)

    def autolabel(rects):
        """Attach a text label above each bar in *rects*, displaying its height."""
        for rect in rects:
            height = rect.get_height()
            ax.annotate('{}'.format(height),
                        xy=(rect.get_x() + rect.get_width() / 2, height),
                        xytext=(0, 3),  # 3 points vertical offset
                        textcoords="offset points",
                        ha='center', va='bottom')


    autolabel(rects1)
    autolabel(rects2)

    fig.tight_layout()

    plt.savefig(img)
    
def stacking(dfAcc1, dfAcc2, img='img.png', color1='blue', color2='orange'):
    labels = ['5', '10', '20', '30']
    acc = dfAcc1['mean']
    dv = dfAcc2['mean']

    x = np.arange(len(labels))  # the label locations
    width = 0.35  # the width of the bars

    fig, ax = plt.subplots()
    rects1 = ax.bar(x - width/2, acc, width, color=color1)
    rects2 = ax.bar(x + width/2, dv, width, color=color2)

    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_ylabel('%')
    ax.set_ylim(0,100)
    #ax.set_title('Scores simples de cada base')
    ax.set_xticks(x)
    ax.set_xticklabels(labels)

    def autolabel(rects):
        """Attach a text label above each bar in *rects*, displaying its height."""
        for rect in rects:
            height = rect.get_height()
            ax.annotate('{}'.format(height),
                        xy=(rect.get_x() + rect.get_width() / 2, height),
                        xytext=(0, 3),  # 3 points vertical offset
                        textcoords="offset points",
                        ha='center', va='bottom')


    autolabel(rects1)
    autolabel(rects2)

    fig.tight_layout()

    plt.savefig(img)