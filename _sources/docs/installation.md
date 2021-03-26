# Installation

Für die Verwendung der Programme aus der Vorlesung werden wir einen Packetmanager installieren. Dieser sorgt dafür, dass wir alle benötigten Bibliotheken einfach in einem definiertem Ecosystem installieren können. 

## Anaconda

Anaconda kann auf folgender Webseite heruntergeladen werden:

[https://www.anaconda.com/products/individual](https://www.anaconda.com/products/individual)

Installieren sie Anaconda nach folgender Anleitung:
- <a href="https://docs.anaconda.com/anaconda/install/windows/" target="_blank">Windows</a>
- <a href="https://docs.anaconda.com/anaconda/install/linux/" target="_blank">Linux</a>

### Erstellen eines Envorinments

Für die Vorlesung werden wir ein Environment erstellen, indem die Aufgaben bearbeitet werden können. Dort werden alle Pakete installiert, die wir verwenden werden.


````{tabbed} Windows (Anaconda Navigator)
1. Öffnen Sie den Anaconda Navigator über die Suchleiste.
<br/><br/><br/>

2. Navigieren Sie zu den Environments.
![cklick_envs](Images_MD/click_environment.png)
<br/><br/><br/>

3. Erstellen Sie nun ein neues Environment mit **Create**.
![create_env](Images_MD/create_new_env.png)
<br/><br/><br/>

4. Tippen Sie den Namen des neuen Environments ein und wählen Sie für **Packages** "Pyhton" aus. Durch klicken auf **Create** wird das neue Environment erstellt.
![apply_new_env](Images_MD/apply_new_env.png)
````

````{tabbed} Windows (Conda Terminal)
Öffnen das Anaconda Promt über die Suchleiste und führen Sie folgenden Befehl aus:
```bash
conda create --name PyVo
```
````

````{tabbed} Linux
Öffnen Sie das Linux Terminal und führen Sie folgenden Befehl aus:
```bash
conda create --name PyVo
```
````
<br/><br/><br/><br/>
### Installation der benötigten Pakete

Für die Scripte werden 3 zusätzliche Pakete und Jupyter-Lab benötigt.

````{tabbed} Windows (Anaconda Navigator)
Um ein neues Paket mit dem Anaconda Navigotor zu installieren sollten sie wie folgt vorgehen: <br/><br/>
**1** Klicken Sie auf das erstellte Environment um es zu aktivieren.\
**2** Ändern Sie die Auflistung der Pakete von **Installed** zu **All**\
**3** Suchen Sie folgende Pakete und wählen Sie diese wie in **4** aus:
- numpy
- matplotlib
- pandas
<br/>

**5** Bestätigen Sie die Auswahl mit **Apply**.

![new_pack](Images_MD/new_pack.png)
<br/><br/><br/>

Mit der Bestätigung wird in einem neuen Fenster aufgelistet, welche zusätzlichen Pakete installiert werden. 

![apply_pck](Images_MD/install_pgk_and_deps.png)
<br/><br/><br/>

Jupyter-Lab kann im Home Menü **1** installiert und gestartet werden.\
Dafür kann einfach unter JupyterLab auf **Install** oder **Launch** **2** geklickt werden.\
Achten Sie darauf, dass unter **3** auch das aktuelle Environment ausgewählt ist.

![launch_JL](Images_MD/install_jl.png)

````

````{tabbed} Windows (Conda Terminal)
- Aktivieren Sie das Environment mit folgendem Befehl:
```bash
conda activate PỳVo
```
- Um die benötigten Pakete zu installieren führen Sie diese Befehle **nacheinander** aus:

```bash
conda install numpy
```
```
conda install matplotlib
```
```
conda isntall pandas
```
```
conda install -c conda-forge jupyterlab
```
- Starten Sie Jupyter Lab mit dem Befehl:
```bash
jupyter-lab
```

````

````{tabbed} Linux
- Aktivieren Sie das environment mit folgendem Befehl:
```bash
conda activate PyVo
```
- Um die benötigten Pakete zu installieren führen Sie diese Befehle **nacheinander** aus:
```bash
conda install numpy
```
```
conda install matplotlib
```
```
conda isntall pandas
```
```
conda install -c conda-forge jupyterlab
```
- Starten Sie Jupyter Lab mit dem Befehl:
```bash
jupyter-lab
```

````