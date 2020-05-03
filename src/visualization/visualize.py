import matplotlib.pyplot as plt
import seaborn as sns


def plot_two_hist(df, attribute, bins=30, figsize=(12, 7)):
    df_bom = df[df['DESEMPENHO'] == 1]
    df_ruim = df[df['DESEMPENHO'] == 0]
    
    fig, axs = plt.subplots(1,2, figsize=(15, 7), sharex=True)
    df_bom[attribute].hist(bins=bins, ax=axs[0], grid=False)
    df_ruim[attribute].hist(bins=bins, ax=axs[1], grid=False)
    
    axs[0].set_title(attribute + ' - desempenho BOM', fontsize=14)
    axs[1].set_title(attribute + ' - desempenho RUIM', fontsize=14)
    
    for ax in axs:
        axs[0].spines['right'].set_visible(False)
        axs[0].spines['top'].set_visible(False)

        axs[1].spines['right'].set_visible(False)
        axs[1].spines['top'].set_visible(False)

        ax.tick_params(axis='x', labelsize=14)
    
    plt.tight_layout()


def plot_kde_two_samples(df, attribute, bw='scott', figsize=(12, 7)):
    df_bom = df[df['DESEMPENHO'] == 1]
    df_ruim = df[df['DESEMPENHO'] == 0]
    
    fig, ax = plt.subplots(figsize=figsize)
    sns.kdeplot(df_bom[attribute], color='b', shade=True, label='BOM', bw=bw) 
    sns.kdeplot(df_ruim[attribute], color='r', shade=True, label='RUIM', bw=bw) 
  
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    
    plt.xlabel(attribute, fontsize=14) 
    plt.ylabel('Densidade de Probabilidade', fontsize=14)


def plot_scatter(df, x, y, figsize=(12, 10)) :
    df_bom = df[df['DESEMPENHO'] == 1]
    df_ruim = df[df['DESEMPENHO'] == 0]
    
    fig, ax = plt.subplots(figsize=figsize)

    df_ruim.plot(kind='scatter', x=x, y=y, c='red', s=40, alpha=0.6, ax=ax, label='RUIM')
    df_bom.plot(kind='scatter', x=x, y=y, c='blue', s=40, alpha=0.6, ax=ax, label='BOM')
    
    ax.set_title('Distribuicao dos dados', fontsize=14)
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    
    ax.tick_params(axis='x', labelsize=12)
    ax.tick_params(axis='y', labelsize=12)
    
    plt.xlabel(x, fontsize=14) 
    plt.ylabel(y, fontsize=14) 


def plot_density_2d(df, x, y, figsize=(12, 10)) :
    df_bom = df[df['DESEMPENHO'] == 1]
    df_ruim = df[df['DESEMPENHO'] == 0]
    
    fig, ax = plt.subplots(figsize=figsize)

    ax = sns.kdeplot(df_bom[x], df_bom[y],
                 cmap="Blues", shade=True, shade_lowest=False, alpha=0.6, label='BOM')

    ax = sns.kdeplot(df_ruim[x], df_ruim[y],
                 cmap="Reds", shade=True, shade_lowest=False, alpha=0.6, label='RUIM')
    
    ax.set_title('Distribuicao dos dados', fontsize=14)
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    
    ax.tick_params(axis='x', labelsize=12)
    ax.tick_params(axis='y', labelsize=12)
    
    plt.xlabel(x, fontsize=14) 
    plt.ylabel(y, fontsize=14) 
    
    plt.legend()