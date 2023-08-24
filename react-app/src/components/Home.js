import React, { Component } from "react";
import { Col, Container, Row } from "reactstrap";

import axios from "axios";

import {VEHICLE_URL} from "../constants";

class Home extends Component {
  state = {
    vehicle: [],
    companyName: [],
  };

  componentDidMount() {
    this.resetState();
  }

  getVehicle = () => {
    axios.get(VEHICLE_URL).then(res => this.setState(
        {
            vehicle: res.data.vehicle_type,
            companyName: res.data.company_name,
            companyColour: res.data.company_brand_colour_main,
            battery: res.data.battery_percentage,
        }
    ));
  };

  resetState = () => {
    this.getVehicle();
  };

  // Very rarely do I usually do inline styling but cut a corner here for speed

  render() {
    return (
      <Container style={{ marginTop: "20px" }}>
        <Row>
          <Col style={{color: this.state.companyColour, textAlign: "center", fontSize: "30px"}}>
              {this.state.companyName}
          </Col>
        </Row>
        <Row>
          <Col>
            Battery
          </Col>
          <Col>
            {this.state.battery}%
          </Col>
        </Row>
        <Row>
          <Col>
            Status
          </Col>
          <Col>
            Charging
          </Col>
        </Row>
        <Row>
          <Col>
              Vehicle Type
          </Col>
          <Col>
            {this.state.vehicle}
          </Col>
        </Row>
      </Container>
    );
  }
}

export default Home;