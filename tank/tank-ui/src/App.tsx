import React, {useEffect, useState} from 'react';

import { ReactComponent as TankIcon } from './tank.svg';
import { ReactComponent as StopIcon } from './stop.svg';
import RotateRightIcon from '@mui/icons-material/RotateRight';
import RotateLeftIcon from '@mui/icons-material/RotateLeft';
import KeyboardDoubleArrowUpIcon from '@mui/icons-material/KeyboardDoubleArrowUp';
import KeyboardDoubleArrowDownIcon from '@mui/icons-material/KeyboardDoubleArrowDown';

import {Joystick} from 'react-joystick-component';
import {IJoystickUpdateEvent} from "react-joystick-component/build/lib/Joystick";
import {moveTankStop} from "./service/moveTankStop";
import {moveTankForward} from "./service/moveTankForward";
import {moveTankReverse} from "./service/moveTankReverse";
import {moveTankRight} from "./service/moveTankRight";
import {moveTankLeft} from "./service/moveTankLeft";
import {moveTankCounterClockwise} from "./service/moveTankCounterClockwise";
import {moveTankClockwise} from "./service/moveTankClockwise";
import {getTankStatus} from "./service/getTankStatus";
import {Direction} from "./Direction";
import {TankStatus} from "./TankStatus";
import styled from "@emotion/styled";
import {Box, Slider, Stack} from "@mui/material";
import {tankSpeedUp} from "./service/tankSpeedUp";
import {tankSpeedDown} from "./service/tankSpeedDown";

const THRESHOLD = 0.3;

function issueCommand(directions: [Direction, Direction]) {
    const [dx, dy] = directions;
    console.log(`issue command, dx: ${dx}, dy: ${dy}`);

    if (dx === Direction.NEUTRAL && dy === Direction.NEUTRAL) { // stop
        moveTankStop();
    }
    if (dx === Direction.NEUTRAL && dy !== Direction.NEUTRAL) { // forward/reverse only
        if (dy === Direction.POSITIVE) {
            moveTankForward();
        } else if (dy === Direction.NEGATIVE) {
            moveTankReverse();
        }
    } else if (dy === Direction.NEUTRAL && dx !== Direction.NEUTRAL) { // left/right only
        if (dx === Direction.POSITIVE) {
            moveTankRight();
        } else if (dx === Direction.NEGATIVE) {
            moveTankLeft();
        }
    }
}

export const App = () => {
    const [directions, setDirections] = useState<[Direction, Direction]>([Direction.NEUTRAL, Direction.NEUTRAL]);
    const [tankStatus, setTankStatus] = useState<TankStatus>({} as TankStatus);
    const [speed, setSpeed] = useState<number>(100);

    useEffect(() => {
        getTankStatus().then((response) => {
            setTankStatus(response.data);
            console.log(response.data);
            // setSpeed(response.data.leftTank.speed);
        });
    }, []);

    const handleEvent = (event: IJoystickUpdateEvent) => {
        const {x, y} = event;
        const dx = getDirection(x!);
        const dy = getDirection(y!);
        //console.log(`x: ${x}, y: ${y}`);
        //console.log(`dx: ${dx}, dy: ${dy}`);

        if (dx !== directions[0] || dy !== directions[1]) {
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
        moveTankStop();
    }

    const handleTankClockwise = async () => {
        await moveTankStop();
        await moveTankClockwise();
    }

    const handleTankCounterClockwise = async () => {
        await moveTankStop();
        await moveTankCounterClockwise();
    }

    // TODO add function to tank to directly set speed, also resolve why tank status is not being parsed correctly.
    const handleSpeedUp = () => {
        if (speed >= 100) { return }

        let newSpeed = speed + 10;
        if (newSpeed >= 100) {
            newSpeed = 100;
        }
        setSpeed(newSpeed);
        tankSpeedUp();
    }

    const handleSpeedDown = () => {
        if (speed <= 0) { return }

        let newSpeed = speed - 10;
        if (newSpeed < 0) {
            newSpeed = 0;
        }
        setSpeed(newSpeed);
        tankSpeedDown();
    }

    // const handleSpeedChange = (event: any) => {
    //     const newSpeed = event.target!.value;
    //     if (Math.floor(newSpeed / 10) !== Math.floor(speed / 10)) {
    //         if (newSpeed > speed) {
    //             tankSpeedUp();
    //         }
    //         else if (newSpeed < speed) {
    //             tankSpeedDown();
    //         }
    //         setSpeed(Math.floor(newSpeed / 10) * 10);
    //     }
    //     console.log(event);
    // }

    return (
        <StyledApp className="app">
            <header className="app-header">
                <TankIcon className="app-logo" />
                <p>
                    Tank v1.0
                </p>
            </header>
            <Box display="flex" flexDirection="column" alignItems="flex-start">
                <div className="controller">
                    {/*<Stack sx={{ height: 256, marginX: 8 }} spacing={1} direction="row">*/}
                    {/*    <Slider*/}
                    {/*        aria-label="Speed"*/}
                    {/*        orientation="vertical"*/}
                    {/*        valueLabelDisplay="auto"*/}
                    {/*        defaultValue={speed || 100}*/}
                    {/*        min={0}*/}
                    {/*        max={100}*/}
                    {/*        onChange={handleSpeedChange}*/}
                    {/*    />*/}
                    {/*</Stack>*/}
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
                            <RotateRightIcon className="rotate-cw"/>
                        </button>
                        <button className="button" onClick={handleStop}>
                            <StopIcon className="stop" />
                        </button>
                        <button className="button" onClick={handleTankCounterClockwise}>
                            <RotateLeftIcon className="rotate-ccw"/>
                        </button>
                    </div>
                    <div className="buttons">
                        <button className="button" onClick={handleSpeedUp}>
                            <KeyboardDoubleArrowUpIcon className="speed-up"/>
                        </button>
                        <Box paddingX={3}>
                            {speed}
                        </Box>
                        <button className="button" onClick={handleSpeedDown}>
                            <KeyboardDoubleArrowDownIcon className="speed-down" />
                        </button>
                    </div>
                </div>

                {/* status */}
                {/*<Box className="status" display="flex" flexDirection="column">*/}
                {/*    <Box display="flex" flexDirection="row">*/}
                {/*        <div>Left Speed: </div>*/}
                {/*        <div>{tankStatus?.leftTank?.speed || 'N/A'}</div>*/}
                {/*    </Box>*/}
                {/*    <Box display="flex" flexDirection="row">*/}
                {/*        <div>Right Speed: </div>*/}
                {/*        <div>{tankStatus?.rightTank?.speed || 'N/A'}</div>*/}
                {/*    </Box>*/}
                {/*</Box>*/}
            </Box>
        </StyledApp>
    );
}
export default App;

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
        width: 64px;
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
          
          svg {
            width: 100%;
            height: 100%;
          }
        }
      }
    }
    
    .status {
      padding: 10px;
    }

  }
`;