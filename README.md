# TestTecnicParlem - DavidRomeroRodriguez
Benvingut al repositori amb la meva versió de la prova tècnica.
En aquesta prova he muntat un servidor de Frontend amb  Angular, i un servidor de Backend amb Flask (Python).

He distribuit el backend en 4 capes diferents per a tractar els objectes de l'aplicació a diferents nivells. En ordre ascendent, aquestes són les capes:
- **model**: Defineix els atributs dels objectes de l'aplicació.
- **persistence**: Agafa del repositori els objectes especificats. En aquest cas, he hardcodejat una llista de objectes per a demostrar el funcionament, pero normalment ho enllaçaria a una base de dades.
- **business**: Crida al repositori per obtenir els objectes, i els tracta/transforma per a que la API els pugui retornar fàcilment.
- **api**: Estableix les rutes/URLs dels diferents mètodes de la API web.
---
### Instal·lació del projecte
El projecte requereix tenir instal·lat [Angular](https://angular.io/guide/setup-local) i [Python 3](https://www.python.org/downloads/). Una vegada es té això instal·lat, seguiu aquests pasos per executar l'aplicació:

1. Obriu una terminal i accediu al directori `/parlem-back`.
2. Executeu la comanda `pip install -r requirements.txt` per instal·lar les dependències del projecte.
3. Executeu la comanda `python run.py` per arrrancar el servidor de back. Si tot va bé, s'hauria d'haver desplegat a http://localhost:5000
4. Sense tancar la terminal, obriu una de nova i accediu al directori `/parlem-front`.
5. Executeu la comanda `ng serve --open`. Si tot va bé, s'hauria d'obrir una web al vostre navegador: http://localhost:4200
6. Si teniu algun problema en el pas 5, proveu a executar `npm install` abans de `ng serve --open`.
---
Per qualsevol dubte, si us plau no dubteu en contactar amb mi al meu correu: [davromrod@gmail.com](mailto:davromrod@gmail.com)
