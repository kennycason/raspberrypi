import React, {useState} from 'react';
import logo from './tank.svg';

import {Joystick} from 'react-joystick-component';
import styled from "styled-components";
import {IJoystickUpdateEvent} from "react-joystick-component/build/lib/Joystick";
import {tankStop} from "./service/tankStop";
import {tankForward} from "./service/tankForward";
import {tankReverse} from "./service/tankReverse";
import {tankRight} from "./service/tankRight";
import {tankLeft} from "./service/tankLeft";

enum Direction {
    POSITIVE = 'POSITIVE',
    NEUTRAL = 'NEUTRAL',
    NEGATIVE = 'NEGATIVE'
}

const THRESHOLD = 0.3;

function issueCommand(directions: [Direction, Direction]) {
    const [dx, dy] = directions;

    if (dx == Direction.NEUTRAL && dy == Direction.NEUTRAL) { // stop
        tankStop();
    }
    if (dx == Direction.NEUTRAL && dy != Direction.NEUTRAL) { // forward/reverse only
        if (dy == Direction.POSITIVE) {
            tankForward();
        } else if (dy == Direction.NEGATIVE) {
            tankReverse();
        }
    }
    else if (dy == Direction.NEUTRAL && dx != Direction.NEUTRAL) { // left/right only
        if (dx == Direction.POSITIVE) {
            tankRight();
        } else if (dx == Direction.NEGATIVE) {
            tankLeft();
        }
    }
}

export const App = () => {
    const [directions, setDirections] = useState<[Direction, Direction]>([Direction.NEUTRAL, Direction.NEUTRAL]);

    const handleEvent = (event: IJoystickUpdateEvent) => {
        const { x, y } = event;
        const dx = getDirection(x!);
        const dy = getDirection(y!);
        console.log(`x: ${x}, y: ${y}`);
        console.log(`dx: ${dx}, dy: ${dy}`);

        if (dx != directions[0] || dy != directions[1]) {
            issueCommand([dx, dy])
        }

        setDirections([dx, dy]);
    }

    const getDirection = (v: number): Direction => {
        if (v > THRESHOLD) {
            return Direction.POSITIVE;
        } else if (v < -THRESHOLD) {
            return Direction.NEGATIVE;
        }
        return Direction.NEUTRAL;
    }

    const handleMove = (event: IJoystickUpdateEvent) => handleEvent(event);

    const handleStop = (event: IJoystickUpdateEvent) => {
        setDirections([Direction.NEUTRAL, Direction.NEUTRAL]);
        tankStop();
    }

    return (
        <StyledApp className="app">
            <header className="app-header">
                <img src={logo} className="app-logo" alt="logo"/>
                <p>
                    Tank v1.0
                </p>
            </header>
            <div className="joystick-container">
                <Joystick
                    size={256}
                    sticky={true}
                    baseColor="#282c34"
                    stickColor="black"
                    move={handleMove}
                    stop={handleStop}
                />
            </div>
        </StyledApp>
    );
}

const StyledApp = styled.div`
  &.app {
    text-align: center;

    .app-header {
      background-color: #282c34;
      padding: 10px;
      padding-right: 20px;
      height: 60px;
      display: flex;
      flex-direction: row;
      align-items: center;
      justify-content: space-between;
      font-size: calc(10px + 2vmin);
      color: white;


      .app-logo {
        height: 64px;
        pointer-events: none;
      }

      @media (prefers-reduced-motion: no-preference) {
        .App-logo {
          animation: App-logo-spin infinite 20s linear;
        }

      }

      @keyframes App-logo-spin {
        from {
          transform: rotate(0deg);
        }
        to {
          transform: rotate(360deg);
        }
      }
    }
    
    
    .joystick-container {
      padding: 20px;
    }
  }
`;