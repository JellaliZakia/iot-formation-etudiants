% ==========================================
% 1. LECTURE DES DONNÉES DEPUIS THINGSPEAK
% ==========================================
channelID = xxxxxxx;             % Remplace par ton ID de canal
readAPIKey = 'xxxxxxxxx';      % Remplace par ta clé de lecture
writeAPIKey = 'xxxxxxxx';     % Remplace par ta clé d'écriture

% Lecture du dernier point reçu (Champ 1: Temp, Champ 2: Humidité, Champ 3: Luminosité)
data = thingSpeakRead(channelID, 'NumPoints', 1, 'ReadKey', readAPIKey);
temp = data(1);       % Température (°C)
humidity = data(2);   % Humidité (%)
light = data(3);      % Luminosité (Lux)

% ==========================================
% 2. LOGIQUE DE DÉCISION (Remplacement de la logique floue)
% ==========================================
% On calcule un temps d'irrigation en minutes (de 0 à 30 min) 
% basé sur les 3 paramètres (Température, Humidité, Luminosité)

if temp >= 35 && humidity < 40
    % Temps très chaud et sol très sec -> Arrosage Long
    decision = 25; 
elseif temp >= 35 && humidity >= 40
    % Chaud mais humidité correcte -> Arrosage Moyen
    decision = 15;
elseif temp >= 25 && temp < 35 && humidity < 40
    % Température moyenne et humidité basse -> Arrosage Moyen
    decision = 12;
elseif temp >= 25 && temp < 35 && humidity >= 40 && humidity < 70
    % Conditions normales -> Arrosage Court
    decision = 5;
elseif humidity >= 70
    % Sol déjà très humide -> Pas d'arrosage
    decision = 0;
else
    % Temps frais ou conditions douces par défaut
    if light > 700 && humidity < 50
        decision = 10; % Un peu de soleil fort, on arrose modérément
    else
        decision = 2;  % Arrosage minimal de maintenance
    end
end
pause(15);

% ==========================================
% 3. ENVOI DU RÉSULTAT VERS THINGSPEAK
% ==========================================
% On écrit le temps d'irrigation calculé dans le Champ 4 (Field 4)
thingSpeakWrite(channelID, decision, 'Fields', 4, 'WriteKey', writeAPIKey);

% Affichage dans les logs MATLAB de ThingSpeak pour vérification
fprintf('Temp: %.1f°C | Hum: %.1f%% | Lum: %.1f Lux ==> Temps d''arrosage : %.1f min\n', temp, humidity, light, decision);
