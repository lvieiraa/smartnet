/*
 * Copyright 2015-present Open Networking Foundation
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
package org.onosproject.metrics.topology.cli;

import java.util.List;
import java.util.regex.Matcher;
import java.util.regex.Pattern;
import com.fasterxml.jackson.databind.JsonNode;
import com.fasterxml.jackson.databind.ObjectMapper;
import com.fasterxml.jackson.databind.node.ArrayNode;
import com.fasterxml.jackson.databind.node.ObjectNode;
import org.apache.karaf.shell.commands.Command;
import org.onosproject.cli.AbstractShellCommand;
import org.onosproject.event.Event;
import org.onosproject.metrics.topology.TopologyMetricsService;

/**
 * Command to show the list of last topology events.
 */
@Command(scope = "onos", name = "topology-lances",
         description = "Lists the last topology events")
public class TopologyEventsFailCommand extends AbstractShellCommand {

    private static final String FORMAT_EVENT =  "Event=%s";
    private static final String FORMAT_REASON = "    Reason=%s";

    @Override
    protected void execute() {
        TopologyMetricsService service = get(TopologyMetricsService.class);
        json(service.getEvents());
     }

    /**
     * Produces a JSON array of topology events.
     *
     * @param events the topology events with the data
     * @return JSON array with the topology events
     */
    private JsonNode json(List<Event> events) {
        ObjectMapper mapper = new ObjectMapper();
        ArrayNode result = mapper.createArrayNode();

        for (Event event : events) {
            result.add(json(mapper, event));
        }
        return result;
    }

    /**
     * Produces JSON object for a topology event.
     *
     * @param mapper the JSON object mapper to use
     * @param event the topology event with the data
     * @return JSON object for the topology event
     */
    private ObjectNode json(ObjectMapper mapper, Event event) {
        ObjectNode result = mapper.createObjectNode();

        result.put("time", event.time())
            .put("type", event.type().toString())
            .put("event", event.toString());
//String que ermazena informacoes de eventos na rede
         String pp =  event.toString();
//Regex para selecionar apenas DeviceEvent
         String pat = "DeviceEvent.*";

   Pattern r = Pattern.compile(pat);
   Matcher m = r.matcher(pp);
   String device = "";
  if (m.find()) {
      //print("%s", m.group(0));
   device = m.group(0);
   result(device);
     }
 //    print("%s", device);
    return result;
    }
    public void result(String device) {
        String[] cada = device.split("=");
        String saida = cada[1] + "---" + cada[11] + cada[12] + cada[13];
        String saida2 = saida.replace("type---of:", "");
        String saida3 = saida2.replace("number", "");
        String saida4 = saida3.replace("isEnabled", "");
        String saida5 = saida4.replace(", type", "");
        String[] saida6 = saida5.split(",");
        String saida7 = saida6[1] + saida6[2] + saida6[3];
 //  print("%s", saida7);
      switch (saida7) {
      case " 0000000000000003 7 true":
      print("CAIU\n");
      break;
      default:
     print("NAO CAIU'\n");
}

  //  print("%s", saida5);
    }
}
