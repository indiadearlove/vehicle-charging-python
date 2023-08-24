import React, { Component } from "react";
import {Button, Col, Container, Row} from "reactstrap";

import axios from "axios";

import {STOP_CHARGE_URL, VEHICLE_URL, START_CHARGE_URL} from "../constants";

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
            status: res.data?.charge?.status,
            startTime: res.data?.charge?.start_time,
            batteryIncrease: res.data?.charge?.estimated_battery_increase_percentage,
        }
    ));
  };

  getStartTime() {
      let date = new Date(this.state?.startTime);
      return date.toLocaleTimeString();
  }

  resetState = () => {
    this.getVehicle();
  };

  stopCharge = e => {
    e.preventDefault();
    axios.get(STOP_CHARGE_URL).then(() => {
      this.resetState();
    });
  }

  startCharge = e => {
    e.preventDefault();
    axios.get(START_CHARGE_URL).then(() => {
      this.resetState();
    });
  }

  pluggedIn() {
      return (
          <div>
              <Row>
                  <Col>
                    Battery Increase
                  </Col>
                  <Col>
                    {this.state.batteryIncrease}%
                  </Col>
                </Row>
                <Row>
                  <Col>
                      {this.state.status == "charging"
                            ? "Status"
                            : "Next Charge"
                      }
                  </Col>
                  <Col>
                      {this.state.status == "charging"
                            ? this.state?.status
                            : this.getStartTime()
                      }
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
                <Row>
                    <Col>
                        {this.state.status == "charging"
                            ? <Button onClick={this.stopCharge}>Stop Charge</Button>
                            : <Button onClick={this.startCharge}>Start Charge</Button>
                        }
                    </Col>
                </Row>
          </div>
      );
  }

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
          {this.state?.status ? this.pluggedIn() : ""}
      </Container>
    );
  }
}

export default Home;