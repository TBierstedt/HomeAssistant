# Home Assistant Blueprints

Hier sammle ich Blueprints für meine eigene Home-Assistant-Instanz. Jede Blueprint bekommt einen eigenen Unterordner unter `blueprints/automation/`, damit Datei und (falls vorhanden) Doku zusammenbleiben.

## Übersicht

| Blueprint | Wofür | Import |
|---|---|---|
| [Shelly Button1 – 4 Klick-Aktionen](blueprints/automation/shelly-button1-4-click-actions/shelly-button1-4-click-actions.yaml) | Löst je nach Klick-Art (einfach / doppelt / dreifach / lang) eines Shelly Button 1 (Gen1, WiFi) eine frei konfigurierbare Aktions-Sequenz aus | [![Import in Home Assistant](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fraw.githubusercontent.com%2FTBierstedt%2FHomeAssistant%2Fmain%2Fblueprints%2Fautomation%2Fshelly-button1-4-click-actions%2Fshelly-button1-4-click-actions.yaml) |

## Installation

Am einfachsten über den Import-Button in der Tabelle – der öffnet direkt den Blueprint-Import-Dialog in Home Assistant.

Falls der Button nicht funktioniert (z. B. weil der Link noch auf einen alten Branch zeigt) oder du lieber manuell vorgehst:

- **Per URL:** In Home Assistant unter *Einstellungen → Automatisierungen & Szenen → Blueprints → Blueprint importieren* die Rohdaten-URL der gewünschten Datei einfügen, z. B.
  `https://raw.githubusercontent.com/TBierstedt/HomeAssistant/main/blueprints/automation/shelly-button1-4-click-actions/shelly-button1-4-click-actions.yaml`
- **Per Datei:** Die `.yaml`-Datei direkt nach `<config>/blueprints/automation/` kopieren und Home Assistant neu starten bzw. die Automatisierungen neu laden.

Danach taucht die Blueprint unter *Einstellungen → Automatisierungen & Szenen → Blueprints* auf und kann als neue Automatisierung angelegt werden.

## Voraussetzungen

- Aktuelle Home-Assistant-Version mit Blueprint-Unterstützung (Standard)
- Für die Shelly-Blueprint zusätzlich: ein per Shelly-Integration eingebundener Shelly Button 1 (Gen1, WiFi)

## Lizenz

[MIT](LICENSE)
