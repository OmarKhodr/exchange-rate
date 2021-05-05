import { useState, useEffect } from "react";
import { Button, Typography, Box, Select, MenuItem, TextField } from '@material-ui/core';

export default function Conversion({ SERVER_URL, rates, back }) {
  let [conversionInput, setConversionInput] = useState(0);
  let [conversionOutput, setConversionOutput] = useState(0);
  let [conversionType, setConversionType] = useState("usd-to-lbp");

  function convert() {
    if (conversionType === "usd-to-lbp") {
      setConversionOutput(conversionInput * rates.usd_to_lbp);
    }
    else {
      setConversionOutput(conversionInput / rates.lbp_to_usd);
    }
  }

  return (
    <div>
      <Typography variant="h5" style={{ fontWeight: 600 }}>Rate Calculator</Typography>
      <form name="conversion-entry">
        <div>
          <TextField
            label={conversionType === "lbp-to-usd" ? "LBP Amount" : "USD Amount"}
            value={conversionInput}
            onChange={e => setConversionInput(e.target.value)}
          />
        </div>
      </form>

      <div>
        <TextField
          label={conversionType !== "lbp-to-usd" ? "LBP Amount" : "USD Amount"}
          InputProps={{ readOnly: true, }}
          value={conversionOutput.toFixed(2)}
        />
      </div>

      <Box my={2}>
        <Select id="conversion-type" value={conversionType} onChange={e => { setConversionType(e.target.value); setConversionOutput(0); setConversionInput(0); }}>
          <MenuItem value="usd-to-lbp">USD to LBP</MenuItem>
          <MenuItem value="lbp-to-usd">LBP to USD</MenuItem>
        </Select>
      </Box>

      <Button id="convert-button" variant="contained" color="primary" onClick={convert}>Convert</Button>

      <div>
        <br/> <br/>
        <Button variant="contained" color="primary" onClick={back}> Back </Button>
      </div>
    </div>
  );
}