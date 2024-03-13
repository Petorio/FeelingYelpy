import React, { Component }from "react";
import Button from "@material-ui/core/Button";
import Grid from "@material-ui/core/Grid";
import Typography from "@material-ui/core/Typography";
import TextField from "@material-ui/core/TextField";

export default class HomePage extends Component {
    constructor(props) {
        super(props);
        this.state = {
            locationValue: ""
        };
        this.handleLocationChange = this.handleLocationChange.bind(this);
        this.handleSearchButtonPressed = this.handleSearchButtonPressed.bind(this);
    }

    handleLocationChange(e) {
        this.setState({
            locationValue: e.target.value,
        });
    }

    handleSearchButtonPressed() {
        const requestOptions = {
            method: "POST",
            headers: { "Content-Type": "application/json"},
            body: JSON.stringify({
                location: this.state.locationValue
            }),
        };
        fetch("/api/create-search", requestOptions)
            .then((response) => response.json())
            .then((data) => console.log(data));
      }


    
    render() {
        return ( 
            <Grid container spacing={1}>
            <Grid item xs={12} align='center'>
                <Typography component="h4" variant="h4">
                    I'm Feeling Yelpy
                </Typography>
            </Grid>
            <Grid item xs={12} align='center'>
                <TextField id="location" type="string" required label="Location" variant="outlined" value={this.state.locationValue} onChange={this.handleLocationChange}/>
            </Grid>
            <Grid item xs={12} align='center'>
                <Button color='primary' variant='contained' onClick={this.handleSearchButtonPressed}>
                    Search
                </Button>
            </Grid>
        </Grid>
        );
    }
}