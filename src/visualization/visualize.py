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
