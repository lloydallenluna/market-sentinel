import json
import os


STATE_FILE = "alert_state.json"


class AlertEngine:

    OVERBOUGHT = 70
    WATCH_OVERBOUGHT = 65

    OVERSOLD = 30
    WATCH_OVERSOLD = 35


    def __init__(self):

        self.states = self.load_states()


    def load_states(self):

        if os.path.exists(STATE_FILE):

            try:
                with open(STATE_FILE, "r") as file:
                    return json.load(file)

            except Exception:
                return {}

        return {}


    def save_states(self):

        with open(STATE_FILE, "w") as file:
            json.dump(
                self.states,
                file,
                indent=4
            )


    def get_state(self, rsi):

        if rsi >= self.OVERBOUGHT:
            return "OVERBOUGHT"

        elif rsi >= self.WATCH_OVERBOUGHT:
            return "WATCH_OVERBOUGHT"

        elif rsi <= self.OVERSOLD:
            return "OVERSOLD"

        elif rsi <= self.WATCH_OVERSOLD:
            return "WATCH_OVERSOLD"

        else:
            return "NORMAL"


    def process(self, symbol, timeframe, rsi):

        key = f"{symbol}_{timeframe}"

        new_state = self.get_state(rsi)

        previous_state = self.states.get(key)


        if previous_state is None:

            self.states[key] = new_state
            self.save_states()

            if new_state == "OVERBOUGHT":
                return "CONFIRMED_OVERBOUGHT"

            elif new_state == "WATCH_OVERBOUGHT":
                return "WATCH_OVERBOUGHT"

            elif new_state == "OVERSOLD":
                return "CONFIRMED_OVERSOLD"

            elif new_state == "WATCH_OVERSOLD":
                return "WATCH_OVERSOLD"

            return None


        if previous_state == new_state:
            return None


        self.states[key] = new_state
        self.save_states()


        if new_state == "OVERBOUGHT":
            return "CONFIRMED_OVERBOUGHT"

        if new_state == "WATCH_OVERBOUGHT":
            return "WATCH_OVERBOUGHT"

        if new_state == "OVERSOLD":
            return "CONFIRMED_OVERSOLD"

        if new_state == "WATCH_OVERSOLD":
            return "WATCH_OVERSOLD"


        return None