import * as React from "react";
import Box from "@mui/material/Box";
import InputLabel from "@mui/material/InputLabel";
import MenuItem from "@mui/material/MenuItem";
import FormControl from "@mui/material/FormControl";
import Select from "@mui/material/Select";
import { useGlobalContext, PICK_YEAR } from "./StateContext";

const BasicSelect = () => {
  const {
    state: { currYear },
    dispatch,
  } = useGlobalContext();

  const handleChange = (event) => {
    dispatch({ type: PICK_YEAR, year: event.target.value });
  };
  const [years, setYears] = React.useState([]);

  React.useEffect(() => {
    // Define the fetch function
    (async () => {
      try {
        const response = await fetch("http://127.0.0.1:5000/years"); // Replace with your API endpoint
        if (!response.ok) {
          throw new Error("Network response was not ok");
        }
        const data = await response.json();
        setYears(data); // Save the result to state
      } catch (error) {
        console.log(error);
      }
    })();
  }, []); // Empty dependency array means this runs once when the component mounts

  return (
    <Box sx={{ minWidth: 120 }}>
      <FormControl fullWidth>
        <InputLabel id="demo-simple-select-label">Years</InputLabel>
        <Select
          labelId="demo-simple-select-label"
          id="demo-simple-select"
          value={currYear}
          label="Years"
          onChange={handleChange}
        >
          {years.map((year) => (
            <MenuItem key={year} value={year}>
              {year}
            </MenuItem>
          ))}
        </Select>
      </FormControl>
    </Box>
  );
};

export default BasicSelect;
