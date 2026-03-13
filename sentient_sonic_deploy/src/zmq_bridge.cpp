/**
 * @file zmq_bridge.cpp
 * @brief Sentient-SONIC ZMQ Communication Bridge
 *
 * Bridges robot state and control commands over ZMQ for
 * distributed deployment and teleoperation.
 *
 * Copyright (c) 2026 Sentient Robotics
 * Licensed under Apache License 2.0
 */

#include <iostream>
#include <string>
#include <thread>
#include <atomic>

namespace sentient {
namespace sonic {

class ZMQBridge {
public:
    ZMQBridge(int state_port = 5555, int command_port = 5556)
        : state_port_(state_port), command_port_(command_port) {}

    ~ZMQBridge() { stop(); }

    bool start() {
        std::cout << "[ZMQ] Starting bridge on ports "
                  << state_port_ << " / " << command_port_ << std::endl;
        running_ = true;
        // Mocked: In production, creates ZMQ PUB/SUB sockets
        return true;
    }

    void stop() {
        running_ = false;
        std::cout << "[ZMQ] Bridge stopped." << std::endl;
    }

    bool is_running() const { return running_; }

private:
    int state_port_;
    int command_port_;
    std::atomic<bool> running_{false};
};

}  // namespace sonic
}  // namespace sentient
