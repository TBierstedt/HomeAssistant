# 🏠 Home Assistant Blueprints

Eine Sammlung eigener Home Assistant Blueprints für Automatisierungen. Jede Blueprint liegt in einem eigenen Unterordner und lässt sich per One-Click-Import direkt in Home Assistant laden.

## 📋 Verfügbare Blueprints

### 🔘 Shelly Button1 – 4 Klick-Aktionen

Reagiert auf 4 Klick-Arten (einfach, doppelt, dreifach, lang) eines Shelly Button 1 (WiFi, Gen1) und führt je Klick-Art eine frei wählbare Aktions-Sequenz aus.

[![Öffne deine Home Assistant Instanz und zeige den Blueprint-Import-Dialog mit vorausgefülltem Blueprint.](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fraw.githubusercontent.com%2FTBierstedt%2FHomeAssistant%2Fclaude%2Fhomeassistant-blueprint-install-phycpv%2Fblueprints%2Fautomation%2Fshelly-button1-4-click-actions%2Fshelly-button1-4-click-actions.yaml)

- **📁 Datei:** [`shelly-button1-4-click-actions.yaml`](blueprints/automation/shelly-button1-4-click-actions/shelly-button1-4-click-actions.yaml)

> Der Import-Badge verweist aktuell auf den Branch `claude/homeassistant-blueprint-install-phycpv`, da dein Repo noch keinen `main`-Branch hat. Sobald dieser Branch in `main` gemergt wird, sollte die `blueprint_url` im Badge-Link (und die URL unten bei Methode 2) entsprechend auf `main` aktualisiert werden.

---

## 🚀 Installation

### Methode 1: One-Click-Import (empfohlen)

1. Auf den Import-Badge der gewünschten Blueprint klicken
2. Deine Home Assistant Instanz öffnet sich mit vorausgefüllter Blueprint
3. Auf "Blueprint importieren" klicken
4. Automatisierung aus der Blueprint anlegen

### Methode 2: Manueller Import per URL

1. Rohdaten-URL der Blueprint kopieren, z. B.:
   ```
   https://raw.githubusercontent.com/TBierstedt/HomeAssistant/claude/homeassistant-blueprint-install-phycpv/blueprints/automation/shelly-button1-4-click-actions/shelly-button1-4-click-actions.yaml
   ```
2. In Home Assistant: **Einstellungen** → **Automatisierungen & Szenen** → **Blueprints** → **Blueprint importieren**
3. URL einfügen und auf "Importieren" klicken

### Methode 3: Lokale Installation

1. Die Blueprint-Datei nach `<config>/blueprints/automation/` kopieren
2. Home Assistant neu starten oder Automatisierungen neu laden
3. Die Blueprint erscheint in der Blueprint-Übersicht

## 🛠️ Voraussetzungen

- Home Assistant mit aktivierter Blueprint-Unterstützung (Standard in aktuellen Versionen)
- Für die Shelly-Blueprint: ein Shelly Button 1 (Gen1, WiFi) als eingebundenes Gerät
