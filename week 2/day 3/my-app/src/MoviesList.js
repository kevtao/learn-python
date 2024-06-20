import React from "react";
import CardContent from "@mui/material/CardContent";
import Typography from "@mui/material/Typography";
import Card from "@mui/material/Card";


const MoviesList = ( {movies, daddy}) => {
  return (
    <div>
      {movies.map((movie, index) => (
        <Card key={index}>
          <CardContent>
            <Typography variant="h5" component="h2">
              {movie.title}
            </Typography>
            <Typography color="textSecondary">Year: {movie.year}</Typography>
            <Typography variant="body2" component="p">
              {movie.description}
            </Typography>
          </CardContent>
        </Card>
      ))}
    </div>
  );
};

export default MoviesList;
