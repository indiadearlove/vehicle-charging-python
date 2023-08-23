import React, { Component } from "react";
import { Col, Container, Row } from "reactstrap";
// import StudentList from "./StudentList";
// import NewStudentModal from "./NewStudentModal";

import axios from "axios";

import { COMPANY_URL } from "../constants";

class Home extends Component {
  state = {
    company: []
  };

  componentDidMount() {
    this.resetState();
  }

  getCompanies = () => {
    axios.get(COMPANY_URL).then(res => this.setState({ company: res.data }));
  };

  resetState = () => {
    this.getCompanies();
  };

  render() {
    return (
      <Container style={{ marginTop: "20px" }}>
        <Row>
          <Col>
            "hello"
          </Col>
        </Row>
        <Row>
          <Col>
            hello
          </Col>
        </Row>
      </Container>
    );
  }
}

export default Home;