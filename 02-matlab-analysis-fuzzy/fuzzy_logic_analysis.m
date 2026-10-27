% Formation IoT - Logique floue
% À coller dans MATLAB Analysis de ThingSpeak

readChannelID = XXXXXXX;
readAPIKey    = 'XXXXXXXXXXXXXXXX';
writeAPIKey   = 'XXXXXXXXXXXXXXXX';

[temp, ~] = thingSpeakRead(readChannelID, 'Fields', 1, 'NumPoints', 10, 'ReadKey', readAPIKey);
[hum, ~]  = thingSpeakRead(readChannelID, 'Fields', 2, 'NumPoints', 10, 'ReadKey', readAPIKey);

if isempty(temp)
    disp('Aucune donnée');
    return;
end

lastTemp = temp(end);
lastHum  = hum(end);

if lastTemp >= 20 && lastTemp <= 26 && lastHum >= 40 && lastHum <= 60
    confort = 1.0; status = "Très confortable";
elseif lastTemp >= 18 && lastTemp <= 28 && lastHum >= 30 && lastHum <= 70
    confort = 0.6; status = "Acceptable";
else
    confort = 0.2; status = "Inconfortable";
end

disp(['Temp : ' num2str(lastTemp) ' °C']);
disp(['Hum  : ' num2str(lastHum) ' %']);
disp(['Confort : ' num2str(confort)]);

thingSpeakWrite(readChannelID, confort, 'Fields', 3, 'WriteKey', writeAPIKey);
