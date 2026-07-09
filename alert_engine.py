class AlertEngine:

    OVERBOUGHT = 70
    WATCH_OVERBOUGHT = 65

    OVERSOLD = 30
    WATCH_OVERSOLD = 35

    def __init__(self):
        # Stores current alert state per coin/timeframe
        self.states = {}

    def determine_state(self, rsi):

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

        new_state = self.determine_state(rsi)

        old_state = self.states.get(key)


        # First time seeing this coin/timeframe
        if old_state is None:

            self.states[key] = new_state

            if new_state == "OVERBOUGHT":
                return "CONFIRMED_OVERBOUGHT"

            if new_state == "WATCH_OVERBOUGHT":
                return "WATCH_OVERBOUGHT"

            if new_state == "OVERSOLD":
                return "CONFIRMED_OVERSOLD"

            if new_state == "WATCH_OVERSOLD":
                return "WATCH_OVERSOLD"

            return None


        # No change
        if old_state == new_state:
            return None


        # ----------------------------
        # MOVING INTO OVERSOLD AREA
        # ----------------------------

        if new_state == "WATCH_OVERSOLD":

            if old_state == "NORMAL":
                self.states[key] = new_state
                return "WATCH_OVERSOLD"


        if new_state == "OVERSOLD":

            if old_state in [
                "NORMAL",
                "WATCH_OVERSOLD"
            ]:
                self.states[key] = new_state
                return "CONFIRMED_OVERSOLD"


        # ----------------------------
        # MOVING INTO OVERBOUGHT AREA
        # ----------------------------

        if new_state == "WATCH_OVERBOUGHT":

            if old_state == "NORMAL":
                self.states[key] = new_state
                return "WATCH_OVERBOUGHT"


        if new_state == "OVERBOUGHT":

            if old_state in [
                "NORMAL",
                "WATCH_OVERBOUGHT"
            ]:
                self.states[key] = new_state
                return "CONFIRMED_OVERBOUGHT"


        # ----------------------------
        # RESET WHEN RSI RETURNS NORMAL
        # ----------------------------

        if new_state == "NORMAL":

            self.states[key] = "NORMAL"


        return None