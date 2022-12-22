import React, {useState} from 'react';
import logo from './tank.svg';
import rotateCw from './rotate-cw.svg';
import rotateCcw from './rotate-ccw.svg';
import stop from './stop.svg';

import {Joystick} from 'react-joystick-component';
import styled from "styled-components";
import {IJoystickUpdateEvent} from "react-joystick-component/build/lib/Joystick";
import {tankStop} from "./service/tankStop";
import {tankForward} from "./service/tankForward";
import {tankReverse} from "./service/tankReverse";
import {tankRight} from "./service/tankRight";
import {tankLeft} from "./service/tankLeft";
import {tankCounterClockwise} from "./service/tankCounterClockwise";
import {tankClockwise} from "./service/tankClockwise";

enum Direction {
    POSITIVE = 'POSITIVE',
    NEUTRAL = 'NEUTRAL',
    NEGATIVE = 'NEGATIVE'
}

const THRESHOLD = 0.3;

function issueCommand(directions: [Direction, Direction]) {
    const [dx, dy] = directions;
    console.log(`issue command, dx: ${dx}, dy: ${dy}`);

    if (dx == Direction.NEUTRAL && dy == Direction.NEUTRAL) { // stop
        tankStop();
    }
    if (dx == Direction.NEUTRAL && dy != Direction.NEUTRAL) { // forward/reverse only
        if (dy == Direction.POSITIVE) {
            tankForward();
        } else if (dy == Direction.NEGATIVE) {
            tankReverse();
        }
    } else if (dy == Direction.NEUTRAL && dx != Direction.NEUTRAL) { // left/right only
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
        const {x, y} = event;
        const dx = getDirection(x!);
        const dy = getDirection(y!);
        //console.log(`x: ${x}, y: ${y}`);
        //console.log(`dx: ${dx}, dy: ${dy}`);

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

    const handleStop = () => {
        setDirections([Direction.NEUTRAL, Direction.NEUTRAL]);
        tankStop();
    }

    const handleTankClockwise = async () => {
      await tankStop();
      await tankClockwise();
    }

    const handleTankCounterClockwise = async () => {
        await tankStop();
        await tankCounterClockwise();
    }

    return (
        <StyledApp className="app">
            <header className="app-header">
                <img src={logo} className="app-logo" alt="logo"/>
                <p>
                    Tank v1.0
                </p>
            </header>
            <div className="controller">
                <div className="joystick-container">
                    <Joystick
                        size={256}
                        sticky={false}
                        throttle={100}
                        baseColor="#282c34"
                        stickColor="black"
                        move={handleMove}
                        stop={handleStop}
                    />
                </div>
                <div className="buttons">
                    <button className="button" onClick={handleTankClockwise}>
                        <img src={rotateCw} className="rotate-cw" alt="Clockwise"/>
                    </button>
                    <button className="button" onClick={handleStop}>
                        <img src={stop} className="stop" alt="Stop"/>
                    </button>
                    <button className="button" onClick={handleTankCounterClockwise}>
                        <img src={rotateCcw} className="rotate-ccw" alt="Counter-Clockwise"/>
                    </button>
                </div>
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

    .controller {
      display: flex;
      flex-direction: row;
      align-items: center;
      justify-content: center;
      
      .joystick-container {
        padding: 20px;
        margin-right: 32px;
      }
      
      .buttons {
        display: flex;
        flex-direction: column;
        align-items: flex-start;
        justify-content: center;
                
        .button {
          height: 64px;
          width: 64px;
          margin: 5px;
        }
      }
      
    }
    
  }
`;